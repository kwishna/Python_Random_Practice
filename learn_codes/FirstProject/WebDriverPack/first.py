import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='E:\chromedriver.exe', desired_capabilities=None)
driver.get("http://www.google.com")

assert "Google" in driver.title

driver.maximize_window()
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys("Krishna")
time.sleep(2)
driver.find_element_by_tag_name("body").click()
submit_btn = driver.find_element_by_name("btnK")
submit_btn.click()

address = driver.find_element_by_id("Wprf1b")
driver.execute_script("arguments[0].scrollIntoView(true)", address)
driver.close()