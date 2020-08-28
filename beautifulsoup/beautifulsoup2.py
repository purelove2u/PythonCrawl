from bs4 import BeautifulSoup
import requests

# 요청 가져오기
url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0011843716&date=20200828&type=1&rankingSeq=1&rankingSectionId=100'
res = requests.get(url)


# BeautifulSoup 객체 생성
soup = BeautifulSoup(res.content, 'html.parser')


# soup 객체를 이용해 파싱하기
# find() : 검색되는 제일 첫번째를 리턴
title = soup.find('h3', id='articleTitle')
print(title)
print(title.string)
print(title.get_text())
