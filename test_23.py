from selenium import webdriver
import time

import math


from selenium.webdriver.support.ui import Select


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	#browser.execute_script("window.scrollBy(0, 100);")

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	#confirm = browser.switch_to.alert
	#confirm.accept()

	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	
	# Ваш код, который заполняет обязательные поля
	
	time.sleep(1)
	
	#browser.implicitly_wait(5)
	
	#button = WebDriverWait(browser, 5).until(
    #    EC.element_to_be_clickable((By.ID, "verify"))
    #)
	
	x_element = browser.find_element_by_id('input_value')
	x = x_element.text
	
	y = calc(x)

	answer = browser.find_element_by_id('answer')
	answer.send_keys(y)
		
	
	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()