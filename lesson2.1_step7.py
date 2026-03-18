from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # найти картинку
    img = browser.find_element(By.ID, "treasure")

    x = img.get_attribute("valuex")
   # print(" x_element)
   # assert x_element is not None, "Value don`t find"

    #значение x
    #x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
   #x = x_element.text

    y = calc(x)

    # ввести ответ в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)


    # выбрать чекбокс и радиобаттон
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()