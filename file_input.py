from selenium import webdriver
import math
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')

    name = browser.find_element_by_name('firstname')
    name.send_keys('Name')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Lastname')
    email = browser.find_element_by_name('email')
    email.send_keys('xergut@mail.ru')

    inp = browser.find_element_by_name('file')
    inp.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



