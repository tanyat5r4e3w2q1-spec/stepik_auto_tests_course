from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    number_x = browser.find_element(By.ID, "input_value")
    x = int(number_x.text)

    # Посчитать математическую функцию от x
    y = calc(x)

    # Проскроллить страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")

    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # выбрать чекбокс и радиобаттон
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()




browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

