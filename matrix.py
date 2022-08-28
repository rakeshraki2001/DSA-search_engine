import math
import os
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

allkeyset = set()
def keywords(filename):
    file = open(filename, "r",encoding="utf8")
    s=file.read()
    s=re.sub('[^A-Za-z]+', ' ', s)
    old=s.replace('\n', ' ').replace('\r', '')
    new=old.split(" ")
    stop_words = set(stopwords.words('english'))
    keys=[]
    for w in new:
        if w not in stop_words:
            keys.append(w)

    for key in keys:
        allkeyset.add(key)  




directory = 'problemstatements'
total_docs=0
# iterate over files in
# that directory
for filename in os.listdir(directory):
    total_docs+=1
    keywords("./problemstatements/" +filename)
    

# print(sorted(allkeyset))
print(len(allkeyset))

#array of dictionaries containing term frequency
tf =[]

for filename in os.listdir(directory):
    total_docs+=1
    file = open("./problemstatements/" +filename,  "r",encoding="utf8")
    doc=file.read()
    doc=re.sub('[^A-Za-z]+', ' ', doc)
    olddocs=doc.replace('\n', ' ').replace('\r', '')
    newdocs=olddocs.split(" ")
    stop_words = set(stopwords.words('english'))
    tdic= dict.fromkeys(allkeyset,0)
    keys=[]
    for w in newdocs:
        if w not in stop_words:
            keys.append(w)
    
    for ke in keys:
        tdic[ke]+=(1/len(keys))
    tf.append(tdic)

#idf
idf= dict.fromkeys(allkeyset,0)
for ke in allkeyset:
    cnt=0
    for dic in tf:
        if(dic[ke]!=0):
            cnt+=1
    idf[ke]=math.log(len(tf)/cnt)
# print(idf)
# print(tf[0])


#tf now stores importance
for i in range(len(tf)):
    for ke in allkeyset:
        temp=tf[i][ke]*idf[ke]
        tf[i][ke]=temp

sdoc = input("Search string")

sdoc=re.sub('[^A-Za-z]+', ' ', sdoc)
oldsdocs=sdoc.replace('\n', ' ').replace('\r', '')
newsdocs=oldsdocs.split(" ")
stop_words = set(stopwords.words('english'))
stf= dict.fromkeys(allkeyset,0)
dockeys=[]
for w in newsdocs:
    if w not in stop_words:
        dockeys.append(w)

print(len(allkeyset))

for ke in dockeys:
    stf[ke]+=(1/len(dockeys))

for ke in allkeyset:
    temp=stf[ke]*idf[ke]
    stf[ke]=temp

# print(stf)

# projection_score={}
# for i in range(len(tf)):
#     sum=0
#     magA=0
#     magB=0
#     for ke in allkeyset:
#         sum+=tf[i][ke]*stf[ke]
#         magA+=(tf[i][ke]**2)
#         magB+=(stf[ke]**2)
    
#     projection_score[i]= sum/math.sqrt(magA*magB)

# print(dict(sorted(projection_score.items(), key=lambda item: item[1])))
