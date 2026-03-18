from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #посчитать сумму чисел на странице
    number1 = browser.find_element(By.ID, "num1").text
    number2 = browser.find_element(By.ID, "num2").text
    x = int(number1) + int(number2)

    # выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(x))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()