# 위키피디아 서울 지하철
# https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0
import requests
from lxml.html import fromstring, tostring

# 모듈로 만들어보기
def info():
    url = "https://ko.wikipedia.org/wiki/서울_지하철"

    res = requests.get(url)
    # print(res.text)
    # print(res.content)  # byte형태로 출력

    # parsing 할 수 있는 구조 생성
    data = fromstring(res.text)


    # img Tag 찾기(xpath)
    # for a in data.xpath("//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[1]/td/a/img"):
    #     print(tostring(a))
    #     print(a.xpath("@src"))



    # css select
    for a in data.cssselect(
        "#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img"
        ):
        print(tostring(a))
        print(a.get('src'))


if __name__ == "__main__":
    info()

