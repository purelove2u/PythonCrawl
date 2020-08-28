# BeautifulSoup : 크롤링 유명 패키지
# 사용하기 쉽고, cssselector, xpath 이용해서 파싱 가능

# 단계
# 요청 가져오기
# BeautifulSoup 객체 생성
# soup 객체를 이용해 파싱하기
from bs4 import BeautifulSoup
import requests

# 요청 가져오기
url = "https://ko.wikipedia.org/wiki/서울_지하철"
res = requests.get(url)

# BeautifulSoup 객체 생성
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
print(type(soup))
print(soup.prettify())

# soup 객체를 이용해 파싱하기
print('head', soup.head)
print()
print('title', soup.title)
print()
print('title 문자열', soup.title.string)
print('title 문자열', soup.title.get_text())



