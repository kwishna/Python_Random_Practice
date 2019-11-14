import unittest
from unittest import TestResult
from selenium import webdriver
from learn_codes.Selenium.SeleniumInAction import selenium_in_action
import json

with open("./Configurations/configuration.json", "r") as f:
    conf = json.load(f)

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._browser = webdriver.Chrome()
        self._sel = selenium_in_action(self._browser)

    def test_something(self) -> None:
        self._sel.open_this_url(conf['url'])
        self.assertEqual('My Store', self._sel.page_title())

    def tearDown(self) -> None:
        self._sel.close_browser()

if __name__ == '__main__':
    unittest.main()
