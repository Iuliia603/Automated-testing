from selenium.webdriver.common.by import By
import time
from Wrapper.Browser import Browser
from Wrapper.UIElement import UIElement as Element
from Wrapper.Header import Header

URL = "https://cleveronly.com/brainbucket/index.php?route=account/login"

def test_login_page():
    browser = Browser(URL)
    driver = browser.get_driver()

    header = Header(browser)
    header.open_login_page()

    Login = Element(browser, By.NAME, "eml")
    Login.enter_text("iuliia60358@gmail.com")

    Password = Element(browser, By.NAME, "password")
    Password.enter_text("123456Z")

    login_bth = Element(browser, By.XPATH, "//*[@id='content']/div/div[2]/div/form/input")
    login_bth.click()

    time.sleep(5)
    browser.shutdown()

if __name__ == "__main__":
    test_login_page()

