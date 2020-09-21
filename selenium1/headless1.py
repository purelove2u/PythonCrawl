# 브라우저를 띄우지 않고 작업하기
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('d:/webdriver/chromedriver.exe', options=options)

driver.get('https://www.daum.net')
print(driver.title)

driver.quit()