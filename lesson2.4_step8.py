from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(x))))


try:

    # открыть страницу
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)

    button_book = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button_book.click()

    button_submit = browser.find_element(By.ID, "solve")
    #button_submit = WebDriverWait(browser, 5).until(
       # EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    #)
    browser.execute_script("arguments[0].scrollIntoView(true);", button_submit)

    # решить капчу
    number_x = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = int(number_x.text)
    result = calc(x)

    input_capcha = browser.find_element(By.ID, "answer")
    input_capcha.send_keys(result)

    # Отправляем заполненную форму
    button_submit.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(60)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

