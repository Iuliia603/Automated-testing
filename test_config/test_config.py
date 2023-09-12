from selenium.webdriver.common.by import By
import time
from Wrapper.Browser import Browser
from Wrapper.UIElement import UIElement as Element
from Wrapper.Header import Header
from Wrapper.Right_menu import RightMenu
from Wrapper.Login_page import LoginPage
from Wrapper.Registrant_page import RegistrationPage
from config.config_reader import ConfigReader

URL = "https://cleveronly.com/brainbucket/index.php?route=account/login"
configs = ConfigReader("config.json")
browser = Browser(URL)

def test_registration_through_dropdown():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    driver = browser.get_driver()

    login_page = LoginPage(browser)
    login_page.open_registration_from_account_dropdown()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Juliia")
    registration_form.enter_last_name("Kartashova")
    registration_form.enter_email("iuliia60358@gmail.com")
    registration_form.enter_telephone("3123405555")
    registration_form.enter_first_line_address("175 W Jackson St")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    registration_form.enter_password("qwerty123")
    registration_form.confirm_password("qwerty123")
    registration_form.agree_to_privacy_policy()
    registration_form.submit_form()

    # successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    # assert successful_registration_title.get_text() == 'Your Account Has Been Created!'
    #
    # successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    # assert successful_registration_subtitle.get_text() == 'Congratulations! Your new account has been successfully created!'

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

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Juliia")
    registration_form.enter_last_name("Kartashova")
    registration_form.enter_email("iuliia60358@gmail.com")
    registration_form.enter_telephone("3123405555")
    registration_form.enter_first_line_address("175 W Jackson St")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    registration_form.enter_password("qwerty123")
    registration_form.confirm_password("qwerty123")
    registration_form.agree_to_privacy_policy()
    registration_form.submit_form()

    # successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    # assert successful_registration_title.get_text() == 'Your Account Has Been Created!'
    #
    # successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    # assert successful_registration_subtitle.get_text() == 'Congratulations! Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()


if __name__ == "__main__":
    test_registration_through_dropdown()
    test_registration_from_right_menu()
