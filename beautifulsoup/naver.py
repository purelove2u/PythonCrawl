import requests
from bs4 import BeautifulSoup
import xlsx_write as excel

# 네이버 가장 많이 본 뉴스 타이틀 추출
res = requests.get('https://news.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')

news_list = soup.select('div#ranking_103 > ul > li > a')

news_lists = list()
# print(news_list)
for i, news in enumerate(news_list, 1):
    print('{} : {}'.format(i, news['title']))
    print("{} : {}".format(i, news.string))
    news_lists.append([news.string])
    
# 엑셀저장 - temp5.xlsx
excel.write_excel_template('temp5.xlsx', '생활 문화', news_lists)