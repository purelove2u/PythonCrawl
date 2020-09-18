import requests
from bs4 import BeautifulSoup
import pprint


naver_open_api = 'https://openapi.naver.com/v1/search/news.json'
param = {'query' : 'android'}
headers = {
    'X-Naver-Client-Id' : 'w4C0xiSWdXipBKnm05dW',
    'X-Naver-Client-Secret' : 'M6HffjZkJX'
}

res = requests.get(naver_open_api, params=param, headers=headers)

# print(res.json())
data = res.json()  # json.loads(data)

# print(data["items"])
# print(data["items"][0])
# print()

# pprint.pprint(data["items"])
for idx, item in enumerate(data["items"], 1):
    print(idx, item["title"], item["link"])
