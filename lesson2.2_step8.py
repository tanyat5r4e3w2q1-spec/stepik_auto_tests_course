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
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # открыть страницу
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control[name='firstname']")
    input1.send_keys("Ivan")

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control[name='lastname']")
    input1.send_keys("Ivanov")

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control[name='email']")
    input1.send_keys("Ivan@mail.ru")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    # *** ИСПРАВЛЕНО: Сначала создаем файл ***
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    # СОЗДАЕМ ПУСТОЙ ФАЙЛ, ЕСЛИ ЕГО НЕТ
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # создаем пустой файл
        print(f"Создан файл: {file_path}")
    else:
        print(f"Файл уже существует: {file_path}")

    # А ТЕПЕРЬ загружаем файл
    uploader = browser.find_element(By.ID, "file")
    uploader.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

