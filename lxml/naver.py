import requests
from lxml.html import fromstring, tostring

def main():
    res = requests.get('https://www.naver.com')
    # 신문사 링크 리스트 얻기
    urls = scrape_news_list_page(res)

    # 링크 리스트 파일 저장하기
    for url in urls:
        with open("d:/download/link1.txt", "a") as f:
            f.write(url + "\n")


def scrape_news_list_page(res):
    # 파싱 구조로 변경
    root = fromstring(res.content)

    urls = []

    for a in root.cssselect('div.thumb_area div.thumb_box div.popup_wrap a:nth-child(3)'):
        url = a.get("href")
        # print(url)
        urls.append(url)

    return urls


if __name__ == "__main__":
    main()
