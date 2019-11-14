from selenium import webdriver


class selenium_in_action:

    def __init__(self, driver=None):
        self.wd = driver
        print(__name__)

    def open_this_url(self, url=None):
        self.wd.get(url)

    def close_browser(self) -> object:
        self.wd.quit()

    def page_title(self):
        # self.wd = webdriver.Chrome()
        return self.wd.title
