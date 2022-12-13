'''
Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
        input1.send_keys('first name')
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second')
        input2.send_keys('last name')
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third')
        input3.send_keys('email')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
        input1.send_keys('first name')
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second')
        input2.send_keys('last name')
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third')
        input3.send_keys('email')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error")

if __name__ == '__main__':
    unittest.main()