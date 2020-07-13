from selenium import webdriver
import time

import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	
	x_element = browser.find_element_by_id('treasure')
	
	x_value = x_element.get_attribute("valuex")
	print("value of X: ", x_value)
	
	y = str(calc(x_value))
	
	input = browser.find_element_by_id('answer')
	input.send_keys(y)
	
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