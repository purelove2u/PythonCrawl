import requests
from bs4 import BeautifulSoup

# 구글 뉴스 클리핑
def main():
    url = 'https://news.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako'

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    news_clipping = data_extract(soup)
    for news_section in news_clipping:
        for k, v in news_section.items():
            print("{} : {}".format(k, v))


def data_extract(soup):
    # 뉴스영역 가져오기
    section = soup.select('div.xrnccd > article')

    # 각 섹션에서 링크, 제목, 내용, 출처, 등록일시 추출
    news = []
    news_item = {}
    base_url = 'https://news.google.com'

    for item in section:
        # 링크와 제목 태그 가져오기
        link_title = item.select_one("h3 a")
        # 뉴스 기사 링크 추출
        news_item['주소'] = base_url + link_title['href'][1:]
        # 제목 추출
        news_item['제목'] = link_title.get_text()
        # 내용 추출
        news_item['내용'] = item.select_one('div > span').get_text()
        # 작성자
        news_item['작성자'] = item.select_one('div > div > a').get_text()
        # 작성일자
        news_item['작성일자_시간'] = item.select("div > div > time")
        # 작성일자와 시간이 없는 뉴스기사가 존재
        if  news_item['작성일자_시간']:
            news_item['작성일자_시간'] = (news_item['작성일자_시간'][0])['datetime'].split('T')
            news_item['작성일자'] = news_item['작성일자_시간'][0]
            news_item['작성시간'] = news_item['작성일자_시간'][1][:-1]
        else:
            news_item['작성일자'] = ""
            news_item['작성시간'] = ""

        # dict 구조로 만든 뉴스기사에 대한 정보를 리스트에 추가
        news.append(news_item)

        news_item = {}

    return news


if __name__ == "__main__":
    main()

