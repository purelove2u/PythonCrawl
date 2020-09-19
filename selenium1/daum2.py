from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("d:/webdriver/chromedriver.exe")

browser.get("https://www.daum.net")

assert "Daum" in browser.title

# 접속한 페이지 소스 가져오기
# print(browser.page_source)
# 페이지 소스에서 원하는 요소를 찾기
# BeautifulSoup 사용
# selenium 사용 - find~~~~

element = browser.find_element_by_name("q")

element.send_keys('아이폰')
element.send_keys(Keys.RETURN)

# 검색결과를 가지고 원하는 요소를 파싱
# 연관검색어 출력
keywords = browser.find_elements_by_css_selector('#recomm_lists_top > span.wsn')
for keyword in keywords:
    print(keyword.text)

# 스크린샷 저장 -> 확장자 선택 가능
browser.save_screenshot('./resources/iphone.jpg')

# 스크린샷 저장 -> 확장자 무조건 png 로 저장됨
browser.get_screenshot_as_file('./resources/iphone.png')


time.sleep(3)
browser.quit()
