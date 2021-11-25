# https://play.google.com/store/movies 할인정보 검색
# selenium과 beautifulsoup 연동한 크롤링 실습

# input box에 텍스트 입력하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time  

#### 동적 페이지 스크롤
from selenium import webdriver
import time  

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument("no-sandbox") 
#options.add_argument('headless')

driver_path = './driver/chromedriver'
chrome = webdriver.Chrome(driver_path, options=options)

# 페이지 이동
url =  "https://play.google.com/store/movies/top"
chrome.get(url)

# 지정한 위치로 스크롤 내리기
# 1920 x 1080 (해당도 위치로  스크롤)
# chrome.execute_script("window.scrollTo(0, 1080)")   #1920* 1080(x, y)
# chrome.execute_script("window.scrollTo(0, 2080)")   #1920* 1080
# chrome.execute_script("window.scrollTo(0, 0)")   #1920* 1080

# 화면 가장 아래로 스크롤 내리기
interval = 2
# chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 현재 document의 높이 반환
def downScroll():
    prev_height =chrome.execute_script("return document.body.scrollHeight")
    while True:
        # 스크롤을 현재 페이지 가장 아래로 내림
        chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # 페이지 로딩 대기
        time.sleep(interval)
        # 현재 문서 높이를 가져와서 저장
        curr_height = chrome.execute_script("return document.body.scrollHeight")
        # 현재 높이와 이전 높이가 같으면 페이지의 마지막이라고 판단함. 반복문 탈출
        if curr_height == prev_height:
            break
        # 이전 높이 변경
        prev_height = curr_height

    print("스크롤 완료")

downScroll()
time.sleep(1)
#chrome.close()
#chrome.quit()

# https://play.google.com/store/movies 할인정보 검색하기

def print_form(title,original_price,cut_price,link):
    forms = f"""
    제목 :{title}
    할인 전 금액 : {original_price}
    할인 후 금액 : {cut_price}
    링크 : https://play.google.com{link}
    """
    print(forms)
    print("-"*100)

from bs4 import BeautifulSoup as bs

# selenium chrome 드라이버로 받은 결과를 beautifulsoup에 전달하여 html 문서로 파싱
soup = bs(chrome.page_source, "html.parser")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격 / 할인 가격
    price = movie.find("div", attrs={"class":"LCATme"})

    print(price)
    print(movie.find_all("span", attrs={"aria-hidden":"true"}))

    if ["SUZt4c","djCuy"] in price.find("span")["class"]:
        # 할인 전 가격
        original_price = price.find("span", attrs={"class":"SUZt4c djCuy"}).get_text()
        # 할인 가격
        cut_price = price.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    else:
        # 할인 전 가격
        original_price = price.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
        # 할인 가격
        cut_price = original_price
    
    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    print_form(title, original_price, cut_price, link)