# Find and load a module given its string name, "math",
# then assign it to a local variable called math.
# 
# Actual behind the scene line
# math = __import__("math")

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

class SeleniumTwo(unittest.TestCase):
	'''
		Identation Is Required For Docs String Also.
		
		This Test Case Is For Selenium Learn With Python.
		Automating A Simple Google Search In Chrome Browser.
		chromedriver Is Expected To Be Present In Path Variable Of The System.
	'''
#class SeleniumTwo():

	url = "https://www.google.co.in"	

	def setUp(self):
		option = webdriver.ChromeOptions()
		option.add_experimental_option('excludeSwitches', ['enable-logging'])
		self.driver = webdriver.Chrome(options=option)
		
	def test(self):
		self.driver.get(SeleniumTwo.url)
		srchbox = self.driver.find_element_by_name('q')
		srchbox.send_keys('Hello Brother Songs')
		srchbox.submit()
		
		result = self.driver.find_elements_by_xpath("//img[contains(@class, 'rISBZc')]")
		print(len(result))
		
		try:
			self.assertIn("Google", self.driver.title)
		
		except AttributeError as e:
			print('Attribute Error Captured!')
		
		else:
			print('No Attribute Error')
			
		finally:
			print('Worked Fine')
		
	def tearDown(self):
		self.driver.close()
		
if __name__ == "__main__":	
	'''
	s = SeleniumTwo()
	s.setUp()
	s.test()
	s.tearDown()
	'''
	unittest.main()