# 네이버 해외 증시 가져오기
import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/")
soup = BeautifulSoup(res.content, "html.parser")

#  div.aside_area.aside_popular > table > tbody > tr:nth-child(1)
global_search = soup.select("div.aside_area.aside_stock > table > tbody > tr")
# print(popular_search)
for tr in global_search:
    # 해외 증시
    stock_name = tr.select_one("a").get_text()
    # 해외 증시 지수
    stock_price = tr.select_one("td").get_text()
    # 증감
    stock_up_down = tr.select_one("td:nth-child(3)").get_text()
    print(stock_name, stock_price, stock_up_down)

popular_search = soup.select("div.aside_area.aside_stock > table > tbody")
print(popular_search[0].get_text())
