# 네이버 주식 인기 종목 가져오기
import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')

#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody
pop_stock = soup.select(
    '#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')
print(pop_stock[0].get_text()) # 요소가 1개인 리스트



#  div.aside_area.aside_popular > table > tbody > tr:nth-child(1)
popular_search = soup.select(
    "div.aside_area.aside_popular > table > tbody > tr"
)# 요소과 여러개인 리스트 (tr여러개)
# print(popular_search)
for tr in popular_search:
    # 종목명
    stock_name = tr.select_one("a").get_text()
    # 현재가격
    stock_price = tr.select_one("td").get_text()
    print(stock_name, stock_price)
