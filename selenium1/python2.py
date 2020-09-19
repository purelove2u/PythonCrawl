from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("d:/webdriver/chromedriver.exe")
browser.implicitly_wait(3)
browser.get("http://www.python.org")

# print(browser.title)
# title 안에 Python 글자가 없으면 에러를 발생시키는 코드
assert "Python" in browser.title

# 찾고자 하는 요소에 name이 있는 경우
# element = browser.find_element_by_name('q')

# id 로 찾고 싶다면?
# element = browser.find_element_by_id('id-search-field')

# class name 으로 찾고 싶다면?
# element = browser.find_element_by_class_name('search-field')

# css selector 로 찾고 싶다면?
# element = browser.find_element_by_css_selector('#id-search-field')

# xpath 로 찾고 싶다면?
element = browser.find_element_by_xpath('//*[@id="id-search-field"]')

# 검색창 초기화
element.clear()
# element.send_keys("kimchi")
element.send_keys("python")
element.send_keys(Keys.RETURN)

# 파싱코드가 들어가기 전 만일 결과가 없다면 에러 발생시키기
assert "No results found." not in browser.page_source

titles = browser.find_elements_by_tag_name("h3")

for title in titles:
    print(title.text)


time.sleep(3)
browser.quit()
