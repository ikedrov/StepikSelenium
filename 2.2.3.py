'''
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'https://suninjuly.github.io/file_input.html'

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("1")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("2")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("3")

    input4 = browser.find_element(By.ID, 'file')
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
