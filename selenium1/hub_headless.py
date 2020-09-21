from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# blog.scrapinghub.com 사이트에서 검색어를 넣고
# 검색결과 중 타이틀 추출하기
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("d:/webdriver/chromedriver.exe", options=options)
driver.get("https://blog.scrapinghub.com/")

# 검색창 찾기
elem = driver.find_element_by_class_name("hs-search-field__input")

# 검색어 넣기
elem.send_keys("scraping")
# 엔터
elem.send_keys(Keys.RETURN)

time.sleep(3)

# 타이틀 추출하기
titles = driver.find_elements_by_css_selector("ul#hsresults > li > a")
for title in titles:
    print(title.text)

driver.quit()
