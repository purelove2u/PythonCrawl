import requests
from bs4 import BeautifulSoup

res = requests.get('https://ko.wikipedia.org/wiki/서울_지하철')
soup = BeautifulSoup(res.content, 'html.parser')

# 첫번째 이미지 가져오기
#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img
img1 = soup.select_one('#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img')
print(img1)

# 두번째 이미지 가져오기
img2 = soup.select_one('#mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img')
print(img2)

print(img1['src'])
print(img2['src'])

print()
links = soup.select('a')
print(len(links))
