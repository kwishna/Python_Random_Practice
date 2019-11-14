from selenium import webdriver
from learn_codes.Selenium import StartSeleniumGrid as s
import subprocess
import time

args = ['python', 'StartSeleniumGrid.py']
subprocess.run(args)

try:
    desired_cap = {
        "browserName": "firefox",
        "version": "",
        "platform": "WINDOWS",
    }
    wd = webdriver.Remote(command_executor='http://192.168.1.17:5555/wd/hub',
                          desired_capabilities=desired_cap)
    wd.get('http://192.168.1.17:4444')
    time.sleep(5)
except Exception as e:
    print(e.__cause__())

finally:
    wd.quit()
    s.stop_process(s.processes)