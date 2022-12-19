from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    item = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')

    assert item, 'no item'




