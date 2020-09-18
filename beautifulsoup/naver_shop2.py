import requests
import pprint

# 네이버 오픈API 를 이용한 쇼핑 정보 가져오기
url = "https://openapi.naver.com/v1/search/shop.json"
headers = {
    "X-Naver-Client-Id": "GRAVYZXY8WQHgZ13OXvV",
    "X-Naver-Client-Secret": "SQRgIq7tkK",
}
param = {"query": "샤오미"}

res = requests.get(url, params=param, headers=headers)

pprint.pprint(res.json())
