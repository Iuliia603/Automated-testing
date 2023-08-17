from Wrapper.Header import Header
from Wrapper.Right_menu import RightMenu
from Wrapper.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
        self.login_btn = Element(browser, By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
        self.email_field = Element(browser, By.ID, 'input-email')
        self.password_field = Element(browser, By.ID, 'input-password')

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()
# email input, password input, login button
    def email_input(self, text):
        self.email_field.enter_text(text)

    def password_input(self, text):
        self.password_field.enter_text(text)

    def login_btn_click(self):
        self.login_btn.click()