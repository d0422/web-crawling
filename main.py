import requests
from bs4 import BeautifulSoup
url='https://www.hankyung.com/economy?page='
res=[]
print("조회하고자 하는 날짜(0000.00.00) : ")
date=input()
page=1
while(page!=0):
    urlx=url+str(page)
    response=requests.get(urlx)
    origin=BeautifulSoup(response.text,'html.parser')
    page += 1
    for t in origin.find_all('span',class_="time"):
        if date!=t.text[:10]:
            page=0
    if page!=0:
        res.append(origin.find_all('h3',class_="tit"))
print(date,end="")
print("의 기사 검색결과 입니다.")
for x in res:
    for t in x:
        print(t.text, end=' ')
        print(t.find('a').get('href'))
