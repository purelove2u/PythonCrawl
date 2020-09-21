from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# blog.scrapinghub.com 사이트에서 검색어를 넣고
# 검색결과 중 타이틀 추출하기

browser = webdriver.Chrome('d:/webdriver/chromedriver.exe')
browser.get(('https://blog.scrapinghub.com'))

element = browser.find_element_by_name('term')
# element = browser.find_element_by_class_name("hs-search-field__input")

element.send_keys('scraping')
element.send_keys(Keys.RETURN)

time.sleep(5)

titles = browser.find_elements_by_css_selector('ul#hsresults > li > a')
for title in titles:
    print(title.text)


browser.quit()
