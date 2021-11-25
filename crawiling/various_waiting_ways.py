from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome("./driver/chromedriver")
chrome.get("http://naver.com")
time.sleep(3)
chrome.implicitly_wait(3) # 크롬드라이브와 통신하는 지점에서 delay

# 지정 요소가 로딩 될 때까지 기다림(예시: 최대 10초 기다림)
WebDriverWait(chrome,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"input[name=query]")))
chrome.close()
