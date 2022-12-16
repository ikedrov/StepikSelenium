'''
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий:

открыть страницу
авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()

@pytest.mark.parametrize('links',  ['https://stepik.org/lesson/236895/step/1',
                                   'https://stepik.org/lesson/236896/step/1',
                                   'https://stepik.org/lesson/236897/step/1',
                                   'https://stepik.org/lesson/236898/step/1',
                                   'https://stepik.org/lesson/236899/step/1',
                                   'https://stepik.org/lesson/236903/step/1',
                                   'https://stepik.org/lesson/236904/step/1',
                                   'https://stepik.org/lesson/236905/step/1'])
class TestPage:


    def test_input_answer(self, browser, links):
        result = ''
        browser.get(links)
        browser.implicitly_wait(10)
        browser.find_element(By.ID, 'ember33').click()

        input1 = browser.find_element(By.ID, 'id_login_email')
        input1.send_keys('***')
        input2 = browser.find_element(By.ID, 'id_login_password')
        input2.send_keys('***')

        browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()
        time.sleep(10)

        answer = math.log(int(time.time()))
        input1 = browser.find_element(By.TAG_NAME, 'textarea')
        input1.send_keys(str(answer))
        time.sleep(5)

        browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
        browser.implicitly_wait(5)

        textarea = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
        message = textarea.text

        if 'Correct!' != message:
            result += message

        assert 'Correct!' == message
        print(result)


if __name__ == '__main__':
    pytest.main()


