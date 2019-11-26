from selenium import webdriver
import time
from random import randint as rnd

try:
    # init block
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    # оперделяем адреса для каждой страницы
    main_link = "http://selenium1py.pythonanywhere.com/ru/"
    books_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/"
    clothing_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/clothing_1/"
    catalogue_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    offers_link = "http://selenium1py.pythonanywhere.com/ru/offers/"

    browser.get(main_link)
    browser.find_element_by_class_name('dropdown-toggle').click()
    browser.find_element_by_xpath('//a[text()="Books"]').click()
    assert browser.current_url == books_link  # сраниваем текущий адрес с верным адресом

    browser.find_element_by_class_name('dropdown-toggle').click()
    browser.find_element_by_xpath('//a[text()="Clothing"]').click()
    assert browser.current_url == clothing_link

    browser.find_element_by_class_name('dropdown-toggle').click()
    browser.find_element_by_xpath('//a[text()="Все товары"]').click()
    assert browser.current_url == catalogue_link

    browser.find_element_by_class_name('dropdown-toggle').click()
    browser.find_element_by_xpath('//a[text()="Предложения"]').click()
    assert browser.current_url == offers_link

finally:
    time.sleep(7)
    browser.quit()
