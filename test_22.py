from selenium import webdriver
import time

import math

from selenium.webdriver.support.ui import Select

import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	
	print(os.path.abspath(__file__))
	print(os.path.abspath(os.path.dirname(__file__)))
	print(os.path.dirname(__file__))
	
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	browser.execute_script("window.scrollBy(0, 100);")

	# Ваш код, который заполняет обязательные поля
	
	x_element = browser.find_element_by_id('input_value')
	x_value = x_element.text
		
	y = str(calc(x_value))
	
	answer = browser.find_element_by_id("answer")
	answer.send_keys(y)

	
	checkbox = browser.find_element_by_id('robotCheckbox')
	checkbox.click()
	
	radio = browser.find_element_by_id('robotsRule')
	radio.click()
	

	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()