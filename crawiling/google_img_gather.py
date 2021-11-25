# 구글 이미지 가져오기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip
from PIL import Image
import create_dir_

search_name = input("검색하고 싶은 키워드 : ")
search_limit = int(input("검색 갯수 입력 : "))
search_url = "https://www.google.com/search?q=" + search_name + "&hl=ko&tbm=isch"

# 크롬 옵션 주기, 크롬을 실행시킬 때 브라우저 함수 실행
options = webdriver.ChromeOptions() # 옵션 객체 생성
options.add_argument("window-size=1000,1000") # 실행 윈도우 크기
options.add_argument("no-sandbox") # 탭 간에 분리 함
options.add_argument("headless")

chrome = webdriver.Chrome(ChromeDriverManager().install(),options=options)
chrome.get(search_url)
chrome.implicitly_wait(2)

image_count = len(chrome.find_elements_by_tag_name("img") )
print("로드된 이미지 개수 : ", image_count)

#파일을 저장하기 위한 디렉토리 생성 함수 호출
search_path = os.path.dirname(os.path.realpath(__file__)) + "/" + search_name + "/"
create_dir_.search_selenium(search_name, search_path)

for i in range(search_limit):
    image = chrome.find_elements_by_tag_name("img")[i]
    image.screenshot(search_path + search_name + str(i) + ".png")

chrome.close()    