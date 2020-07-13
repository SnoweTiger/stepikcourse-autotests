from selenium import webdriver
import time

import math

from selenium.webdriver.support.ui import Select

import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	browser.execute_script("window.scrollBy(0, 100);")

	# Ваш код, который заполняет обязательные поля
	
	a = browser.find_element_by_name('firstname')
	a.send_keys('a')
	b = browser.find_element_by_name('lastname')
	b.send_keys('b')
	c = browser.find_element_by_name('email')
	c.send_keys('c')
		
		
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'txt.txt')
	print(file_path)
	element = browser.find_element_by_id('file')
	element.send_keys(file_path)
	
	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()