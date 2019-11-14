from selenium import webdriver
import json
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By

with open('Configurations/configuration.json', 'rb') as f:
    conf = json.load(f)

browser = webdriver.DesiredCapabilities().CHROME

op = options.Options()
op.headless = True

wd = webdriver.Chrome(executable_path='E:\\chromedriver.exe', options=op, desired_capabilities=browser)
wd.get(conf['url'])
wd.find_element(By.CLASS_NAME, "")

print(wd.get_cookies())

wd.quit()

