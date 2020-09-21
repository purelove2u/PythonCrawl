# 다음 댓글 가져오기

# wait : 데이터들이 로드되는 시점의 차이가 존재하는 걸 처리
# implicit wait : 웹페이지 내의 요소를 찾기 위해 web driver가 일정시간 기다리도록 요청
# explicit wait : web driver가 실행을 계속하기 전에 특정 조건이 발생할 때까지 기다리는 것


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")
driver.get("https://news.v.daum.net/v/20200921140716557")

# 더보기 버튼은 댓글이 없는 경우 생성되지 않는 버튼이기 때문에
# 더보기 버튼이 생긴 경우 클릭하라고 코딩해야 함 => explicit wait 사용
loop, count = True, 0

while loop and count < 10:
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.alex_more > button")
            )
        )
        more_button = driver.find_element_by_css_selector(
            "div.alex_more > button"
        )
        more_button.click()
        count += 1
        time.sleep(2)
    except TimeoutException as e:
        print(e)
        loop = False


driver.quit()
