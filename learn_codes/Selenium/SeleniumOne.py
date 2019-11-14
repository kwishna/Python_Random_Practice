from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome('E:\\chromedriver.exe')
chrome.get("https://www.google.co.in")

searchBox = chrome.find_element_by_name("q")
searchBox.send_keys("Himanshu Mishra")

submitBtn = chrome.find_element_by_name("btnK")
submitBtn.submit()
# searchBox.sendkeys(Keys.ENTER)

results = chrome.find_elements_by_class_name("r")
print(len(results))

chrome.close()