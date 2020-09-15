import requests
from bs4 import BeautifulSoup


res = requests.get("https://ko.wikipedia.org/wiki/서울_지하철")
soup = BeautifulSoup(res.content, "html.parser")

# 첫번째 이미지 가져오기
img1 = soup.select_one(
    "#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img"
)

# 해당 사진 저장
download = requests.get('https:' + img1.get('src'))
with open('d:/download/subway.jpg', 'wb') as f:
    f.write(download.content)
    