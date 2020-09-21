# 브라우저를 띄우지 않고 작업하기
from selenium import webdriver

options = webdriver.ChromeOptions()

# 브라우저 안 띄우기
options.add_argument("headless")

# 그래픽카드 사용 안하기
options.add_argument('disable-gpu')

# 브라우저 크기 지정
options.add_argument('windows-size=1920*1080')

# user-agent 지정
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')

driver = webdriver.Chrome("d:/webdriver/chromedriver.exe", options=options)

driver.get("http://www.daum.net")

print(driver.title)


driver.quit()
