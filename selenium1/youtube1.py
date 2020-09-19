from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 웹 드라이버 로드
driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")

# 크롤링 대상 사이트 접속
driver.get("https://www.youtube.com")

# 테스트 코드
assert 'YouTube' in driver.title

# 원하는 요소 찾기
element = driver.find_element_by_name('search_query')

# 검색어 넣기
element.send_keys('아이유')

# 엔터치기
element.send_keys(Keys.RETURN)

# 결과 페이지에서 동영상 타이틀 추출 후 출력하기
titles = driver.find_elements_by_tag_name('h3')

for title in titles:
    print(title.text)

time.sleep(5)

# 드라이버 종료
driver.quit()
