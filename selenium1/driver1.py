# 웹드라이버 테스트
from selenium import webdriver
import time

browser = webdriver.Chrome('d:/webdriver/chromedriver.exe')
browser.implicitly_wait(3)
browser.maximize_window()

browser.get('https://www.daum.net')
print(browser.current_url)
print(browser.title)

time.sleep(3)

browser.quit()
