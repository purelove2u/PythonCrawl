from bs4 import BeautifulSoup
import requests

with open("./beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 모든 a 태그 찾기
# find_all() : 필터 기준에 맞는 모든 태그 가져오기
print(soup.find('a'))
print(soup.find_all('a'))
print(soup.find_all('a', limit=2))