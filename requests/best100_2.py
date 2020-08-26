# 다음 쇼핑 베스트 100에서 임의의 카테고리 2개를 정해서
# 정보를 가져온 뒤 상품명 출력하기
# shopping100.py 참고

import requests

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?durationDays=30&count=100"
params = [
    {"vCateId" : "B02", "_" : "1598407715680"}, 
    {"vCateId" : "E01", "_" : "1598407715681"}
    ]

with requests.Session() as s:
    for param in params:
        res = s.get(url, params=param)

        for i, item in enumerate(res.json(), 1):
            if i < 101:
                print(i, item["product_name"])
