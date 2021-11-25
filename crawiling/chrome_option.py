from selenium import webdriver
import time # 셀레니움 실행 시 기다려야하는 시간들이 있음.

# 크롬 옵션 주기, 크롬을 실행시킬 때 브라우저 함수 실행
options = webdriver.ChromeOptions() # 옵션 객체 생성
options.add_argument("window-size=1000,1000") # 실행 윈도우 크기
options.add_argument("no-sandbox") # 탭 간에 분리 함

chrome = webdriver.Chrome("./chromedriver", options=options)
chrome.get("http://naver.com") # 브라우저로 url 실행
time.sleep(3)
chrome.close()