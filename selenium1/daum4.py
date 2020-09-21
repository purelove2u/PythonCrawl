from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# daum.net 접속 후 맨 처음 나오는 뉴스 기사 클릭하여
# 타이틀 추출하기

driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")
driver.get("https://www.daum.net/")

article = driver.find_element_by_css_selector("ul.list_thumb > li > a > div")
article.click()

# 타이틀 추출
element = driver.find_element_by_tag_name("h3")
print(element.text)

time.sleep(3)
driver.quit()
