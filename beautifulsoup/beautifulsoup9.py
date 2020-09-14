# 다음뉴스 가져오기
import requests
from bs4 import BeautifulSoup

url = 'https://news.v.daum.net/v/20200914092607955'
res = requests.get(url)

# 가져온 뉴스를 파싱하기
soup = BeautifulSoup(res.content, 'html.parser')

# 확인
#print('data', soup.prettify())

# 뉴스 제목 가져오기

# title = soup.find('h3')
title = soup.select_one('h3')

print('신문기사 타이틀 : {}'.format(title.string))
print('신문기사 타이틀 : {}'.format(title.get_text()))


# 기사 작성 시간 가져오기
# date = soup.find('span', {'class':'num_date'})
# print('기사작성시간 : {}'.format(date.string))
# date_time = soup.find("span", class_="num_date")
# print('기사작성시간 : {}'.format(date_time.string))
# date_time = soup.find("span", "num_date")
date_time = soup.select_one("span.num_date")
print('기사작성시간 : {}'.format(date_time.string))

# 기사의 첫번째 문단 가져오기
# first_set = soup.find('p', {'dmcf-pid':'AOO7pYADmt'})
# print('첫번째 문단 : {}'.format(first_set.string))
# paragraph1 = soup.find("p", attrs={"dmcf-pid": "AOO7pYADmt"})
paragraph1 = soup.select_one("p[dmcf-pid='AOO7pYADmt']")
print("첫번째 문단 : {}".format(paragraph1.get_text()))