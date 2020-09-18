import requests
import openpyxl
import pprint

#### 네이버 오픈API에서 도서정보 가져와서 엑셀에 저장
## 도서저보 - isbn, title, price, discount
## 필드명 - 번호, isbn, 도서명, 가격, 할인가격

# 엑셀 파일 열기
excel_file = openpyxl.Workbook()
sheet1 = excel_file.active
sheet1.column_dimensions['B'].width = 40
sheet1.column_dimensions['C'].width = 70
sheet1.column_dimensions['D'].width = 20
sheet1.column_dimensions['E'].width = 20
sheet1.column_dimensions['F'].width = 20
sheet1.append(['번호', 'ISBN', '도서명', '작가', '가격', '할인가격'])
sheet1.title = '유시민 관련 도서 목록'

url = 'https://openapi.naver.com/v1/search/book.json'

header ={
    "X-Naver-Client-Id": "GRAVYZXY8WQHgZ13OXvV",
    "X-Naver-Client-Secret": "SQRgIq7tkK",
}

start, num = 1, 0

for idx in range(5):
    start_num = start + (idx * 100)
    param = {
        'query' : '유시민',
        # 'd_auth' : '유시민',
        'display' : 100,
        'start' : start_num
    }
    res = requests.get(url, params=param, headers=header)
    # pprint.pprint(res.json())
    data = res.json()

    if res.status_code == 200:
        for item in data['items']:
            num += 1
            book_info = [num, item['isbn'], item['title'], item['author'], item['price'], item['discount']]
            sheet1.append(book_info)
    else:
        print('Error : ', res.status_code)

excel_file.save('./resources/유시민.xlsx')
excel_file.close()