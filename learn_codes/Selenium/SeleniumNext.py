from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

try:
    b = Chrome()
    b.get('http://automationpractice.com/index.php')
    b.maximize_window()
    women = b.find_element_by_css_selector("ul[class*='menu-content'] > li > a[title='Dresses']")
    a = ActionChains(b)
    a.move_to_element(women).click().perform()

    wait = WebDriverWait(timeout=15, driver=b)
    wait.until(E.visibility_of_any_elements_located((By.CSS_SELECTOR, '.content_scene_cat_bg')))

    drpdwn = Select(b.find_element_by_css_selector('#selectProductSort'))
    drpdwn.select_by_value('name:asc')

except Exception as e:
    print('Exception')
    print(e)

finally:
    time.sleep(10)
    b.quit()