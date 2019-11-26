from selenium import webdriver
import time

try:
    # init block
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)
    query = 'test'  # строка для поиска
    search = browser.find_element_by_css_selector('#id_q')
    search.send_keys(query)
    browser.find_element_by_xpath('//input[@value="Найти"]').click()
    header = f'Товары, соответствующие запросу "{query}"'  # ожидаемый заголовок результатов
    assert header == browser.find_element_by_css_selector('div.page-header h1').text
finally:
    time.sleep(7)
    browser.quit()
