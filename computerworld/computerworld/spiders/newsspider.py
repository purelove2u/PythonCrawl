import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = "newsspider"
    allowed_domains = ["computerworld.com/news/"]
    start_urls = ["https://computerworld.com/news/"]

    def parse(self, response):
        # print("url : {}".format(response.url))

        # 기사의 타이틀 가져오기
        article_titles = response.css(
            "div.river-well div.post-cont h3 a::text"
        ).getall()

        # 세부 기사 링크 가져오기
        article_links = response.css(
            'div.river-well figure a::attr("href")'
        ).getall()

        # 기사 이미지 주소 가져오기
        article_images = response.css(
            'div.river-well figure a img::attr("data-original")'
        ).getall()

        article_contents = response.css(
            "div.river-well div.post-cont h4::text"
        ).getall()

        print("article links {}".format(article_links))
        print("article_titles {}".format(article_titles))
        print("article_images {}".format(article_images))
        print("article_contents {}".format(article_contents))
