import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\\chromedriver.exe")
driver.get("https://www.google.com")
driver.close()