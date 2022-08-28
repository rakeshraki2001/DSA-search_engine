import math
import os
import re
import nltk
from numpy import append
nltk.download('stopwords')
from nltk.corpus import stopwords

keys_set = set()
def keywords(filename):
    file = open(filename, "r",encoding="utf8")
    s=file.read()
    s=re.sub('[^A-Za-z]+', ' ', s)
    old_string=s.replace('\n', ' ').replace('\r', ' ')
    state_string=old_string.split("Example")
    new_string=state_string[0].split(" ")
    stop_words = set(stopwords.words('english'))
    keys=[]
    for w in new_string:
        if w not in stop_words:
            keys.append(w)

    for key in keys:
        keys_set.add(key)


def tf_of(filename):
    file = open(filename,  "r",encoding="utf8")
    doc=file.read()
    doc=re.sub('[^A-Za-z]+', ' ', doc)
    doc=doc.replace('\n', ' ').replace('\r', '')
    state_doc=doc.split("Example")
    split_doc= state_doc[0].split(" ")
    stop_words = set(stopwords.words('english'))
    tdic= dict.fromkeys(sorted(keys_set),0)
    keys=[]
    for w in split_doc:
        if w not in stop_words:
            keys.append(w)
    
    for ke in keys:
        tdic[ke]+= (1/len(keys))
    tf_doc.append(tdic)

#Forming the key_set

directory = 'Problemstatements'
total_docs=0
# iterate over files in that directory
for filename in os.listdir(directory):
    total_docs+=1
    keywords("./Problemstatements/" +filename)

keys_set=sorted(keys_set)

tf_doc =[]

#Calculating Term frequencies
for filename in os.listdir(directory):
    tf_of("./Problemstatements/" +filename)

#Inverse Frequencies
idf= dict.fromkeys(keys_set,0)
for ke in keys_set:
    cnt=0
    for dic in tf_doc:
        if(dic[ke]!=0):
            cnt+=1
    idf[ke]=math.log(len(tf_doc)/cnt)

#Calculating Importance
score_keys = []
print(tf_doc[0])
for i in range(len(tf_doc)):
    temp_arr=[]
    temp_arr.clear()
    for ke in keys_set:
        temp=tf_doc[i][ke]*idf[ke]
        temp_arr.append(temp)
    score_keys.append(temp_arr)
    
        
# print(score_keys[0])
print("Total number of keys",len(keys_set))
# print(keys_set)

#input
sdoc = input("Search string")

sdoc=re.sub('[^A-Za-z]+', ' ', sdoc)
oldsdocs=sdoc.replace('\n', ' ').replace('\r', ' ')
newsdocs=oldsdocs.split(" ")
stop_words = set(stopwords.words('english'))
stf= dict.fromkeys(keys_set,0)

dockeys=[]
for w in newsdocs:
    if w not in stop_words:
        dockeys.append(w)

search_score=[]
for ke in dockeys:
    if ke in stf.keys():
        stf[ke]+=(1/len(dockeys))

for ke in keys_set:
    temp=stf[ke]*idf[ke]
    search_score.append(temp)



#Alignment score

projection_score={}

for i in range(len(score_keys)):
    sum=0
    magA=0
    magB=0
    for j in range(len(search_score)):
        sum+=search_score[j]*score_keys[i][j]
        magA+=(score_keys[i][j]**2)
        magB+=(search_score[j]**2)
    
    projection_score[i+1]= (sum)/(math.sqrt(magA*magB))

print(dict(sorted(projection_score.items(), key=lambda item: item[1])))

