import requests
from bs4 import BeautifulSoup
import openpyxl

##### 엑셀파일
gmarket_best100 = openpyxl.Workbook()

sheet1 = gmarket_best100.active
sheet1.title = '컴퓨터_전자'
sheet1.column_dimensions['A'].width = 10
sheet1.column_dimensions['B'].width = 70
sheet1.column_dimensions['C'].width = 15
sheet1.column_dimensions['D'].width = 80
sheet1.column_dimensions['E'].width = 30
sheet1.append(['순위', '제품명', '할인가', '바로가기', '회사명'])



# g마켓 컴퓨터/전자 베스트 크롤링
url = "http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06"

# 상품명 가격 추출
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

product_list = soup.select('div.best-list')
# best-list 클래스명이 2개가 나옴, 그 중에서 2번째 것만 사용
first_best = product_list[1]
product_list = first_best.select('ul > li')

for i, item in enumerate(product_list, 1):
    # print(i, item.prettify())
    product_name = item.select_one('a.itemname')
    sale_price = item.select_one('div.s-price > strong').text
    # 상세 페이지를 위한 주소 추출
    product_url = product_name['href']
    # 제품 상세 페이지 요청하기
    detail_product = requests.get(product_url)
    company_info = BeautifulSoup(detail_product.content, 'html.parser')
    company_name = company_info.select_one('div.item-topinfo_headline > p > a > strong')

    # print('{} | {} | 할인가 : {} | 바로가기 : {} | 회사명 : {}'.format(i, product_name.text, sale_price, product_url, company_name.text))
    sheet1.append([i, product_name.text, sale_price, product_url, company_name.text])
    
gmarket_best100.save('./resources/gmarket_best.xlsx')
gmarket_best100.close()