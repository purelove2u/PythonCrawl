# 다나와 사이트에서 관심상품 정보 가져오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

# 파싱 라이브러리
from bs4 import BeautifulSoup


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

# 크롬 브라우저 내부 대기
driver.implicitly_wait(3)
driver.get("http://www.danawa.com/")

# 테스트 코드
# print(driver.title)
assert "다나와" in driver.title

# 로그인 버튼 클릭
login = driver.find_element_by_css_selector(
    "div.my_service_list > ul > li.my_page_service > a"
)
login.send_keys(Keys.RETURN)
time.sleep(2)

# 로그인 페이지에서 로그인 정보 입력 후 페이지 이동
# 아이디 란에 본인 아이디 입력하기
id = driver.find_element_by_id("danawa-member-login-input-id")
id.clear()
id.send_keys("pjky5")

# 비밀번호 란에 본인 비밀번호 입력하기
pwd = driver.find_element_by_id("danawa-member-login-input-pwd")
pwd.clear()
pwd.send_keys("12344321@a")
# 로그인 버튼 클릭하기
pwd.send_keys(Keys.RETURN)

# --------------------------------------------- 로그인 성공

# 검색어 넣기
search = driver.find_element_by_id("AKCSearch")
search.clear()
search.send_keys("세탁기")
search.send_keys(Keys.RETURN)
time.sleep(3)

# ---------------------------------------------- 검색결과

# 제조사 클릭
driver.find_element_by_xpath(
    "//*[@id='SearchOption_Maker_Rep']/div[1]/div/label/span[1]"
).click()

# 품목 클릭
# //*[@id="newSearchOptionArea"]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div/label/span[1]
driver.find_element_by_xpath(
    "//*[@id='newSearchOptionArea']/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div/label/span[1]"
).click()

# 세탁 용량 클릭 -> 더보기 클릭
WebDriverWait(driver, 2).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//*[@id='newSearchOptionArea']/div[2]/div[2]/div[4]/div[1]/div[2]/div[2]/button[1]",
        )
    )
).click()

# 세탁용량 목록 중에서 18kg 클릭하기
driver.find_element_by_xpath(
    "//*[@id='SearchOption_RepOption_92_All']/div/div[10]/div/label/span"
).click()

# ------------------------------------------------- 상품 리스트 출력

time.sleep(2)
# 첫번째 상품을 선택 후 상세페이지로 들어가기
driver.find_element_by_css_selector(
    "div.prod_main_info > div.prod_info > p > a"
).click()

# 새 창으로 제어권 넘기기
driver.switch_to.window(driver.window_handles[1])

# 관심버튼 클릭
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#interest > span.ico"))
).click()

# 관심상품을 어디에 담을 것인지 보여주는 리스트 선택하기
WebDriverWait(driver, 2).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "dl.wish_folder > dd > ul > li > a")
    )
).click()

# 관심상품 리스트로 가기 클릭
driver.find_element_by_css_selector("div.folder_submit > div > a").click()

# 관심상품 리스트 페이지에서 상품목록 출력하기
soup = BeautifulSoup(driver.page_source, "html.parser")

wishlist = soup.select("table.wish_tbl > tbody > tr")

for idx, item in enumerate(wishlist, 1):
    product_name = item.select_one("td.info > div.tit > a").text
    product_spec = item.select_one("dl.spec > dd > a").text
    product_price = item.select_one("td.lowest > dl > dd > span").text

    print("[{}] {}".format(idx, product_name))
    print("{}".format(product_spec))
    print("{}".format(product_price))
    print()

time.sleep(3)
driver.quit()
