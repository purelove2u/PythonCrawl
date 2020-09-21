from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
# 브라우저 안 띄우기
# options.add_argument("headless")
# 그래픽 카드 사용 안하기
options.add_argument("disable-gpu")
# 브라우저 크기 지정
options.add_argument("window-size=1920,1080")
# user-agent 지정
options.add_argument(
    "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
)

driver = webdriver.Chrome("d:/webdriver/chromedriver.exe", options=options)
driver.get("https://twitter.com/")

# 아이디
userid = driver.find_element_by_name("session[username_or_email]")
userid.clear()
userid.send_keys('purelove2u')

# 비밀번호
userpwd = driver.find_element_by_name("session[password]")
userpwd.clear()
userpwd.send_keys('wbelansel03-')
userpwd.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()
