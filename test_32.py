import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


import unittest

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'

class TestAbs(unittest.TestCase):
	def test_test1(self):
		browser = webdriver.Chrome()
		browser.get(link1)

		input1 = browser.find_element_by_class_name('first')

		input1.send_keys("Gohn")
		# input2 = browser.find_element_by_class_name('second')
		input1 = browser.find_element_by_css_selector('input[class="second" required="true"]')
		input2.send_keys("Smit")
		input3 = browser.find_element_by_class_name('third')

		input3.send_keys("LA")

		button = browser.find_element_by_css_selector('button[type="submit"]')
		button.click()
		time.sleep(1)

		response_element = browser.find_element_by_tag_name('h1')
		respons = response_element.text
		self.assertEqual(respons,
		'Congratulations! You have successfully registered!',
		"Should be 'Congratulations'")

	def test_test2(self):
		browser = webdriver.Chrome()
		browser.get(link2)

		input1 = browser.find_element_by_class_name('first')
		input1.send_keys("Gohn")
		input2 = browser.find_element_by_class_name('second')
		input2.send_keys("Smit")
		input3 = browser.find_element_by_class_name('third')
		input3.send_keys("LA")

		button = browser.find_element_by_css_selector('button[type="submit"]')
		button.click()
		time.sleep(1)

		response_element = browser.find_element_by_tag_name('h1')
		respons = response_element.text
		self.assertEqual(respons,
		'Congratulations! You have successfully registered!',
		"Should be 'Congratulations'")

		# Отправляем заполненную форму
		# button = browser.find_element_by_css_selector("button.btn")
		# button.click()

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
