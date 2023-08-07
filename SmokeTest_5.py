from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from Wrapper.Browser import Browser
from Wrapper.UIElement import UIElement as Element
from Wrapper.Dropdown import Dropdown
# 07/26 Julia
from Wrapper.Header import Header
from Wrapper.Right_menu import RightMenu
from  Wrapper.Footer import Footer
# 07/26 Julia
URL = "https://cleveronly.com/brainbucket/index.php?route=account/login"
def test_registration_through_dropdown():
    browser = Browser(URL)
    driver = browser.get_driver()

    header = Header(browser)
    header.open_registration_form()

    registration_form_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert registration_form_title.get_text() == 'Register Account'

    inputs = {
        "firstname": "Julia",
        "lastname": "Kartashova",
        "email": 'iuliia60358@gmail.com',
        "telephone": "89764235891",
        "address_1": "675 PA",
        "city": "Pittsburgh",
        "password": "78456Z",
        "confirm": "78456Z"
    }

    for field, text in inputs.items():
        input_field = Element(browser, By.NAME, field)
        input_field.enter_text(text)

    Dropdown(browser, By.ID, "input-country").select_by_value("223")
    Dropdown(browser, By.ID, "input-zone").select_by_text("Pennsylvania")

    #clicking on subscribe YES radio button
    subscribe_r_btn = driver.find_element(by=By.XPATH, value='//*[@id="content"]/form/fieldset[4]/div/div/label[2]')
    if not subscribe_r_btn.is_selected():
        subscribe_r_btn.click()
    privacy_cb = driver.find_element(by=By.NAME, value="agree")
    if not privacy_cb.is_selected():
        privacy_cb.click()

    time.sleep(5)
    browser.shutdown()

def test_registration_from_right_menu():
    browser = Browser(URL)
    driver = browser.get_driver()

    # in Account dropdown select Login option
    header = Header(browser)
    header.open_login_page()

    # click on Register btn in the right menu
    right_menu = RightMenu(browser)
    right_menu.click_registration()

    registration_form_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert registration_form_title.get_text() == 'Register Account'

    inputs = {
        "firstname": "Julia",
        "lastname": "Kartashova",
        "email": 'iuliia60358@gmail.com',
        "telephone": "89764235891",
        "address_1": "675 PA",
        "city": "Pittsburgh",
        "password": "78456Z",
        "confirm": "78456Z"
    }

    for field, text in inputs.items():
        input_field = Element(browser, By.NAME, field)
        input_field.enter_text(text)

    Dropdown(browser, By.ID, "input-country").select_by_value("223")
    Dropdown(browser, By.ID, "input-zone").select_by_text("Pennsylvania")

    # clicking on subscribe YES radio button
    subscribe_r_btn = driver.find_element(by=By.XPATH, value='//*[@id="content"]/form/fieldset[4]/div/div/label[2]')
    if not subscribe_r_btn.is_selected():
        subscribe_r_btn.click()

    Element(browser, By.NAME, "agree").click()

    time.sleep(5)
    browser.shutdown()

def test_registration_from_footer():
    browser = Browser(URL)
    driver = browser.get_driver()

    footer = Footer(browser)
    footer.click_my_account()


if __name__ == "__main__":
    test_registration_through_dropdown()
    test_registration_from_right_menu()
    test_registration_from_footer()