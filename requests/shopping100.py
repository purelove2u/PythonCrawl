# 다음 쇼핑 best100 가져오기
import requests


url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1598323566428"
with requests.Session() as s:
    res = s.get(url)
    # print(res.json())
    for i, item in enumerate(res.json(), 1):
        if i < 101:
            print(i, item["product_name"])
