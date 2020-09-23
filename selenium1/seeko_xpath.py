from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")

driver.get("https://seeko.earlyadopter.co.kr/bbs/board.php?bo_table=mainnews")

# title xpath : //*[@id="fboardlist"]/div[1]/ul/li[3]/div[2]/a
titles = driver.find_elements_by_xpath("//div[@class='wr-subject']/a")

for title in titles:
    print(title.text)

driver.quit()
