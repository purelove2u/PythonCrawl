import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 네이버 접속 후 검색어 넣고 페이지 이동하는 코드

browser = webdriver.Chrome('d:/webdriver/chromedriver.exe')
browser.implicitly_wait(3)
browser.get('https://www.naver.com')

assert "NAVER" in browser.title

element = browser.find_element_by_name('query')

element.clear()
element.send_keys('python')
element.send_keys(Keys.RETURN)

# 파싱코드가 들어가기 전 만일 결과가 없다면 에러 발생시키기
assert "No results found." not in browser.page_source

titles = browser.find_elements_by_css_selector(
    '#main_pack > div.sp_post.section > ul > li:nth-child(1) > dl'
    )

for title in titles:
    print(title.text)

time.sleep(5)
browser.quit()

