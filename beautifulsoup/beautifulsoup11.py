import requests
from bs4 import BeautifulSoup

res = requests.get('http://pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(res.content, 'html.parser')

# Totally Normal Gifts 가져오기
title = soup.select_one('h1')
print('title : {}'.format(title.string))
print()

# 첫번째 문단 가져오기(Here is ....)
first_paragraph = soup.select_one("div[id = 'content']")
print('fist_paragraph : {}'.format(first_paragraph.get_text()))
para1 = soup.find("div", id="content")
print("문단 {}".format(para1.get_text()))
print()
para2 = soup.select_one("div#content")
print("문단 {}".format(para2.get_text()))
print()

# 모든 img 태그 가져오기
imgs1 = soup.find_all("img")
print(imgs1)
print()
imgs2 = soup.select("img")
print(imgs2)
print()
all_img = soup.find_all('img')
for n in all_img:
    print(n['src'])

# 테이블 내용 가져오기
all_table = soup.find_all('td')
for n in all_table:
    print(n.get_text())

print('*' * 50)

contents = soup.select("table#giftList")
for content in contents:
    print(content.get_text())
