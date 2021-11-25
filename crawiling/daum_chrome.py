from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time 
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("http://daum.net")
elem= chrome.find_element_by_class_name("link_login")
elem.click()
chrome.find_element_by_class_name("btn_g").click()
chrome.back()
time.sleep(2)
chrome.forward()
time.sleep(2)

chrome.back()
time.sleep(2)
elem= chrome.find_element_by_name("q")
elem.send_keys("사과")
time.sleep(2)
elem.send_keys("바나나")
time.sleep(2)
chrome.find_element_by_id("q").clear()
elem.send_keys("사과")
time.sleep(2)
elem.send_keys(Keys.ENTER) 
items = chrome.find_elements_by_class_name("thumb_img")

for item in items:
    print(item.get_attribute("src"))
# chrome.close()
