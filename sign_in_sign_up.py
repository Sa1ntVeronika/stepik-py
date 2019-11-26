from selenium import webdriver
import time
from random import randint as rnd

try:
    # init block
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)
    email = f'test{str(rnd(0, 999999999))}@mail.ru'  # создаём случайного пользователя
    password = '284619735'
    success = 'Спасибо за регистрацию!'
    greetings = 'Рады видеть вас снова'
    browser.find_element_by_id('login_link').click()
    browser.find_element_by_id('id_registration-email').send_keys(email)
    browser.find_element_by_id('id_registration-password1').send_keys(password)
    browser.find_element_by_id('id_registration-password2').send_keys(password)
    browser.find_element_by_name('registration_submit').click()  # регистрируемся
    assert success == browser.find_element_by_css_selector('div.alertinner.wicon').text  # проверяем, успешно или нет

    browser.find_element_by_id('logout_link').click()  # выходим из-под учётки
    browser.find_element_by_id('login_link').click()
    browser.find_element_by_id('id_login-username').send_keys(email)
    browser.find_element_by_id('id_login-password').send_keys(password)
    browser.find_element_by_name('login_submit').click()  # логинимся

    assert greetings == browser.find_element_by_css_selector('div.alertinner.wicon').text  # проверяем, залогинились или нет

finally:
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
