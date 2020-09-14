import requests
from bs4 import BeautifulSoup

# 데이터 가져오기
with open('./beautifulsoup/story.html', 'r') as f:
    html = f.read()

# 가져온 데이터 확인하기
# print(html)

# 파싱하기
soup = BeautifulSoup(html, 'html.parser')

link1 = soup.find('a')
print(link1)

link2 = soup.find('a', {'class':'sister'})
print(link2)

link3 = soup.find('a', {'class':'sister', 'data-io':'link3'})
print(link3)