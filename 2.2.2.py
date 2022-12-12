'''
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,'input_value')
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
    radiobutton = browser.find_element(By.ID, 'robotsRule').click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
