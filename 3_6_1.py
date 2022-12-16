from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time

try:
    browser = webdriver.Chrome()

    link = 'https://stepik.org/lesson/236895/step/1'
    browser.get(link)
    browser.implicitly_wait(10)
    enter = browser.find_element(By.ID, 'ember33').click()

    input1 = browser.find_element(By.ID, 'id_login_email')
    input1.send_keys('***')
    input2 = browser.find_element(By.ID, 'id_login_password')
    input2.send_keys('***')

    browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()


finally:
    time.sleep(5)
    browser.quit()


