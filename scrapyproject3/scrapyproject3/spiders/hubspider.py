import scrapy


class HubspiderSpider(scrapy.Spider):
    name = "hubspider"
    # allowed_domains = ["blog.scrapinghub.com"]
    # start_urls = ["https://blog.scrapinghub.com/"]

    def parse(self, response):
        # 상세기사로 들어갈 수 있는 주소 추출
        urls = response.css(
            "div.post-item > div.post-header > h2 > a::attr('href')"
        ).extract()

        for url in urls:
            # print(url)
            # 얻어낸 상세기사 주소를 다시 크롤링 해야 함 => 재귀순회
            yield scrapy.Request(url, self.parse_article)

    def parse_article(self, response):
        # 상세기사 내용 추출
        contents = response.css("div.post-body > span > p::text").getall()
        # print(contents[:100])
        yield {"contents": "".join(contents)}
