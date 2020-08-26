# 크롤링(정보 수집)
# 웹에서 정보 가져오기(urllib, requests)
# 가져온 정보 중에서 유용한 내용 추출(파싱) - lxml
from lxml.html import tostring, fromstring
import requests


def main():
    url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=025&aid=0003029370"
    res = requests.get(url)

    print("res.text : {}".format(type(res.text)))
    print("res content : {}".format(type(res.content)))

    # html 문서 구조 생성
    html_content = fromstring(res.text)
    # print(html_content)
    data_extract(html_content)

def data_extract(html_content):
    # 신문기사 타이틀 출력
    # cssselect()안에는 css 선택자 모두 가능
    title = html_content.xpath('//*[@id="articleTitle"]')
    print("title {}".format(type(title)))
    print("title {}".format(title))
    print("title {}".format(title[0].text_content()))
    print("title {}".format(title[0].text))

    # 기사 속 이미지 가져오기
    images = html_content.xpath(
        # '//*[@id="articleBodyContents"]/div[1]/div/span[1]/img'
        '//*[@id="articleBodyContents"]/div/div/span[@class="end_photo_org"]/img'
    )
    for image in images:
        print(image.get("src"))

if __name__ == "__main__":
    main()
