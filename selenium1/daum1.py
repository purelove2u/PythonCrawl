from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import pprint


browser = webdriver.Chrome('d:/webdriver/chromedriver.exe')

browser.get('https://www.daum.net')

assert 'Daum' in browser.title

# 접속한 페이지 소스 가져오기
# pprint.pprint(browser.page_source)

# 페이지 소스에서 원하는 요소를 찾기
# 1. BeautifulSoup 사용
# 2. selenium 사용 - find~~~~ 에서 다 가능

element = browser.find_element_by_name('q')
element.send_keys('아이폰')
element.send_keys(Keys.RETURN) # 엔터입력과 같은 의미

# 검색 결과를 가지고 원하는 요소를 파싱



time.sleep(3)
browser.quit()
