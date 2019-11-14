from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    chrome = webdriver.Chrome(executable_path='E:\\chromedriver.exe')
    chrome.get(url='http://inst.eecs.berkeley.edu/~cs61a/fa18/')
    print(chrome.title)
    list  = chrome.find_elements(By.XPATH, '//li/a[text()="8pp"]/@href') # Invalid Xpath
    print(len(list))
#    chrome.execute_script('window.open("https://www.google.co.in", "_blank")')

except Exception as e:
    print(e)

finally:
    chrome.quit()
