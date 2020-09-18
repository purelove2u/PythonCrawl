from selenium import webdriver
import time

browser = webdriver.Chrome("d:/webdriver/chromedriver.exe")
browser.implicitly_wait(3)
browser.get('http://www.python.org')

# print(browser.title)
# title 안에 Python 이라는 글자가 없으면 에러를 발생시키는 코드
assert 'Python' in browser.title

time.sleep(3)
browser.quit()
