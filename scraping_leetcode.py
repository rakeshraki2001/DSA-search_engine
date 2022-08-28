from importlib.resources import path
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://leetcode.com/tag/array/")

time.sleep(15)


html= driver.page_source
soup=BeautifulSoup(html,'html.parser')
rows=soup.find_all('tr')
print(len(rows))

#urls to scrape
urls=[]
for i in range(1,len(rows)):
    q=rows[i].find_all('td')[2].find("a")
    link="https://leetcode.com"+q['href']
    urls.append(link)

question_path="D:\VS code\Search Engine project\Problemstatements"
title_path="D:\VS code\Search Engine project\Titles"
url_path="D:\VS code\Search Engine project\Links"

q_number=557
for i in range(715,len(urls)):
    driver.get(urls[i])
    time.sleep(1)
    q_html= driver.page_source
    soup=BeautifulSoup(q_html,'html.parser')
    
    try:
        ptext = soup.find('div', { "class" : "content__u3I1 question-content__JfgR"}).text
        ttext = soup.find('div', { "class" : "css-v3d350"}).text
        q_number+=1
        file_name = "problem"+str(q_number)+".txt"
        with open(os.path.join(question_path, file_name), "w+", encoding="utf-8") as fp:
            fp.write(ptext)
        with open(os.path.join(title_path, file_name), "w+", encoding="utf-8") as fp:
            fp.write(ttext)
        with open(os.path.join(url_path, file_name), "w+", encoding="utf-8") as fp:
            fp.write(urls[i])
    except:
        continue
