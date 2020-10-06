import scrapy

# Selector
# response.css() / response.xpath()
# getall() == extract() /  get() == extract_first()


class SchoolSpider(scrapy.Spider):
    name = "school"
    allowed_domains = ["w3schools.com"]
    start_urls = ["https://w3schools.com/"]

    def parse(self, response):
        # 메뉴 추출하기
        # menu_lists = response.css("nav#mySidenav > div > a::text").getall()
        # menu_lists = response.xpath(
        #     "//nav[@id='mySidenav']/div/a/text()"
        # ).getall()
        menu_lists = response.xpath(
            "//nav[@id='mySidenav']/div/a/text()"
        ).extract()

        for i, title in enumerate(menu_lists, 1):
            print("{} : {}".format(i, title))
            # 파일로 저장
            yield {"no": i, "title": title}
