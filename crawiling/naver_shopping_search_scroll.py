# input box에 텍스트 입력하기
from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")  # 크롬 창을 안뜨게함.
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome = webdriver.Chrome(ChromeDriverManager().install(),options=options)
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("http://shopping.naver.com")
search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name=query]")))
search.send_keys("아이폰 케이스")
time.sleep(2)
search.send_keys("\n")

items = short_wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div[class ^= basicList_info_area__")))

for item in items:
    # 광고 걸러내기
    try:
        item.find_element_by_css_selector("button[class ^= ad_]")
        continue
    except:
        pass
    print(item.find_element_by_css_selector("a[class ^= basicList_link__]").text)

# javascript 실행 문구
# 스크롤 내리는 
# chrome.execute_script("window.scrollBy(0,1000)")

# chrome.execute_script("window.scrollBy(0,document.body.scrollHeight)")

for i in range(8):
    chrome.execute_script("window.scrollBy(0,"+ str((i+1) *1000) + ")")
    time.sleep(1) # loading 할때까지 기다려줌.

items = short_wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR,"div[class ^= basicList_info_area__")))

for item in items:
    # 광고 걸러내기
    try:
        item.find_element_by_css_selector("button[class ^= ad_]")
        continue
    except:
        pass
    print(item.find_element_by_css_selector("a[class ^= basicList_link__]").text)