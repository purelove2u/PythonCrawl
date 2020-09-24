import scrapy


class Hubspider1Spider(scrapy.Spider):
    name = 'hubspider1'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        # print(response.text)
        # print("response url : {}".format(response.url))
        # print("dir : {}".format(dir(response)))
        # print("status : {}".format(response.status))
        # print("body : {}".format(response.body))

        # 타이틀 추출
        titles = response.css('div.post-header > h2 > a::text').getall()

        # 날짜 추출
        dates = response.css('div.post-header > div.byline > span.date > a::text').getall()

        # 작성자 추출
        authors = response.css('div.post-header > div.byline > span.author > a::text').getall()


        for idx, title in enumerate(titles, 0):
            # print('title : {}'.format(title))
            # print('date : {}'.format(dates[idx].strip()))
            # print('author : {}'.format(authors[idx]))
            yield{
                'title' : title,
                'date' : dates[idx].strip(),
                'author' : authors[idx]
            }
