import scrapy


class Hubspider2Spider(scrapy.Spider):
    # 스파이더 명
    name = "hubspider2"
    # 크롤링이 허용된 도메인
    allowed_domains = ["blog.scrapinghub.com", "naver.com", "daum.net"]
    # 시작 주소
    start_urls = [
        "https://blog.scrapinghub.com/",
        "https://www.naver.com",
        "https://www.daum.net",
    ]

    def parse(self, response):
        print("respons url : {}".format(response.url))
