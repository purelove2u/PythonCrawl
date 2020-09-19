from selenium import webdriver
import time

# 드라이버 로드
driver = webdriver.Chrome('d:/webdriver/chromedriver.exe')

# 원하는 사이트 접속
driver.get('https://google.com')

# 현재 접속한 창에 대한 정보 출력
print('title : {}'.format(driver.title))

# 부모창 정보 가져오기
parent_window = driver.current_window_handle
print('parent window : {}'.format(parent_window))

# 자바 스크립트로 새로운 창 열기
driver.execute_script('window.open("https://www.naver.com")')

# 현재 브라우저에 열린 모든 창의 정보
all_windows = driver.window_handles

# 자식 창에 대한 정보 가져오기
child_window = [window for window in all_windows if window != parent_window][0]
print('child window info : {}'.format(child_window))
print('child title : {}'.format(driver.title))  # google

# 자식창으로 제어권 넘겨주기
driver.switch_to.window(child_window)
print('child title : {}'.format(driver.title))  # NAVER

time.sleep(5)

# 드라이버 종료
driver.quit()
