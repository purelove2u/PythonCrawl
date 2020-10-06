import scrapy


class Hubspider1Spider(scrapy.Spider):
    name = "hubspider1"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = ["https://blog.scrapinghub.com/"]

    def parse(self, response):
        # print(response.text)
        # print("response url : {}".format(response.url))
        # print("dir : {}".format(dir(response)))
        # print("status : {}".format(response.status))
        # print("body : {}".format(response.body))

        # 타이틀 추출
        titles = response.css("div.post-header > h2 > a::text").getall()
        # 날짜 추출
        dates = response.css(
            "div.post-header > div.byline > span.date > a::text"
        ).getall()

        for idx, title in enumerate(titles, 0):
            # print("title : {}".format(title))
            # print("date : {}".format(dates[idx]))
            yield {"title": title, "date": dates[idx]}

