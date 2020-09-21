from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 다나와 사이트에서 자동 로그인하기
driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")
driver.get("http://www.danawa.com/")
# driver.get('https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F')

# 로그인 버튼 클릭
login_button = driver.find_element_by_css_selector('li.my_page_service > a')
login_button.click()


# 아이디 란에 본인 아이디 입력하기
id_element = driver.find_element_by_name('id')
id_element.clear()
id_element.send_keys('purelove2u')

# 비밀번호 란에 본인 비밀번호 입력하기
password_element = driver.find_element_by_name('password')
password_element.send_keys('wbelansel03!')

# 로그인 버튼 클릭하기
login_confirm = driver.find_element_by_id('danawa-member-login-loginButton')
login_confirm.click()


time.sleep(5)

driver.quit()