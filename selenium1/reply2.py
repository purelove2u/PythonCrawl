# 다음 댓글 가져오기 - 최신순 댓글 가져오기
# Waits : 데이터들이 로드되는 시점의 차이가 존재하는 걸 처리
# implicit wait : 웹페이지 내의 요소를 찾기 위해 web driver가 일정시간 기다리도록 요청
# explicit wait : web driver가 실행을 계속하기 전에 특정 조건이 발생할 때까지 기다리는 것


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

chromedriver = "d:/webdriver/chromedriver.exe"
headless_options = webdriver.ChromeOptions()
# headless_options.add_argument("headless")  # --headless 도 됨
# 그래픽 카드 쓰지 않겠다
headless_options.add_argument("disable-gpu")
# 클라이언트 요청
headless_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
)
# 브라우저 크기 지정
headless_options.add_argument("window-size=1920,1080")
# 사용자가 쓰는 언어
headless_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(chromedriver, chrome_options=headless_options)

driver.get("https://news.v.daum.net/v/20200921140716557")

# 최신순 클릭하기

# 최신순 버튼이 보여질때까지 기다린 후 클릭하기
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.cmt_box > ul > li:nth-child(3)")
    )
).click()

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

# 댓글 가져오기
comment_lists = driver.find_elements_by_css_selector(
    "ul.list_comment > li > div > p"
)

for num, comment in enumerate(comment_lists, start=1):
    print("[{}] : {}".format(num, comment.text))


driver.quit()
