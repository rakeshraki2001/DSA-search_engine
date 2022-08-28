from importlib.resources import path
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://leetcode.com/tag/array/")
# driver.get("https://www.codechef.com/tags/problems/dynamic-programming")

time.sleep(15)

html= driver.page_source
soup=BeautifulSoup(html,'html.parser')
rows=soup.find_all('tr')
print(len(rows))
urls=[]
titles=[]
for i in range(1,len(rows)):
    q=rows[i].find_all('td')[2].find("a")
    link="https://leetcode.com"+q['href']
    urls.append(link)
    titles.append(q.text)



path="D:\VS code\Search Engine project\problemstatements"
for i in range(len(urls)):
    driver.get(urls[i])
    time.sleep(1)
    qhtml= driver.page_source
    soup=BeautifulSoup(qhtml,'html.parser')
    
    file_name = "problem"+str(i+1)+".txt"
    try:
        ptext = soup.find('div', { "class" : "content__u3I1 question-content__JfgR"}).text
        ttext = soup.find('div', { "class" : "css-v3d350"}).text
        print(ttext[1])
        # with open(os.path.join(path, file_name), "w+", encoding="utf-8") as fp:
        #     fp.write(ptext)
    except:
        continue