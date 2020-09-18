import requests
# from bs4 import BeautifulSoup
import pprint
import openpyxl

# 엑셀 저장
excel_file = openpyxl.Workbook()

sheet1 = excel_file.active
sheet1.column_dimensions['B'].width = 100
sheet1.column_dimensions['C'].width = 60
sheet1.append(['순위', '상품명', '주소'])
sheet1.title = '샤오미 top1000'

# 네이버 오픈 API 를 이용한 쇼핑 정보 가져오기
naver_open_api = 'https://openapi.naver.com/v1/search/shop.json'
headers = {
    'X-Naver-Client-Id' : 'w4C0xiSWdXipBKnm05dW',
    'X-Naver-Client-Secret' : 'M6HffjZkJX'
}

start, num = 1, 0
for idx in range(10):
    start_num = start + (idx * 100)
    param = {
        'query' : '샤오미',
        'display' : 100,
        'start' : start_num
    }
    res = requests.get(naver_open_api, params=param, headers=headers)

    # print(res.json())
    # pprint.pprint(res.url)
    
    data = res.json()
    if res.status_code == 200:
        for item in data['items']:
            num += 1
            product_info = [num, item['title'], item['link']]
            sheet1.append(product_info)
    else:
        print('Error ', res.status_code)

excel_file.save('./resources/샤오미.xlsx')
excel_file.close()
