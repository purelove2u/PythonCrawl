import scrapy


class GspiderSpider(scrapy.Spider):
    name = "gspider"
    allowed_domains = ["corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers/"]

    def parse(self, response):
        print("response.url : {}".format(response.url))

        # ALL 제품 목록 출력하기
        titles = response.css(
            "div.best-list > ul[class!=plus] > li > a::text"
        ).getall()

        for idx, title in enumerate(titles, 1):
            print("{}. {}".format(idx, title))
