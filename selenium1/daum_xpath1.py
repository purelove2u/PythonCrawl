from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome("d:/webdriver/chromedriver.exe", options=options)

driver.get("https://news.v.daum.net/v/20200921140716557")

# 타이틀 가져오기
# //*[@id="cSub"]/div/h3
print(driver.find_element_by_xpath("//*[@id='cSub']/div/h3").text)

driver.quit()
