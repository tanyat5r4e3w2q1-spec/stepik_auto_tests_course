from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(x))))


try:

    # открыть страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажать на кнопку
    button_trollface = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button_trollface.click()

    # переключиться на новую вкладку
    first_window = browser.window_handles[0]  # имя текущей вкладки
    new_window = browser.window_handles[1] # имя новой вкладки
    browser.switch_to.window(new_window)

    # решить капчу
    number_x = browser.find_element(By.ID, "input_value")
    x = int(number_x.text)
    result = calc(x)

    input_capcha = browser.find_element(By.ID, "answer")
    input_capcha.send_keys(result)

    # Отправляем заполненную форму
    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button_submit.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

