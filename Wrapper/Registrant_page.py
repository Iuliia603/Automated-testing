from Wrapper.Header import Header
from Wrapper.Right_menu import RightMenu
from Wrapper.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from Wrapper.Dropdown import Dropdown
from Wrapper.Chekbox import Checkbox


class RegistrationPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)

        self.title = Element(browser, By.XPATH, "//*[@id='content']/h1")
        self.first_name_input = Element(browser, By.NAME, "firstname")
        self.last_name_input = Element(browser, By.NAME, "lastname")
        self.email_input = Element(browser, By.NAME, "email")
        self.telephone_input = Element(browser, By.NAME, "telephone")
        self.fax_input = Element(browser, By.NAME, "fax")
        self.company_input = Element(browser, By.NAME, "company")
        self.first_address_input = Element(browser, By.NAME, "address_1")
        self.city_input = Element(browser, By.NAME, "city")
        self.postcode_input = Element(browser, By.NAME, "postcode")
        self.password_input = Element(browser, By.NAME, "password")
        self.confirm_password_input = Element(browser, By.NAME, "confirm")

        self.country_dropdown = Dropdown(browser, By.ID, 'input-country')
        self.region_dropdown = Dropdown(browser, By.NAME, 'zone_id')

        self.subscribe_btn = Checkbox(browser, By.XPATH, "//input[@name='newsletter' and @value='1']")
        self.unsubscribe_btn = Checkbox(browser, By.XPATH, "//input[@name='newsletter' and @value='0']")

        self.privacy_policy_checkbox = Checkbox(browser, By.NAME, "agree")

        self.contniue_btn = Element(browser, By.XPATH, "//input[@value='Continue']")

    def get_form_title(self):
        return self.title.get_text(wait=True)

    def enter_first_name(self, text):
        self.first_name_input.enter_text(text)

    def enter_last_name(self, text):
        self.last_name_input.enter_text(text)

    def enter_email(self, text):
        self.email_input.enter_text(text)

    def enter_telephone(self, text):
        self.telephone_input.enter_text(text)

    def enter_fax(self, text):
        self.fax_input.enter_text(text)

    def enter_company(self, text):
        self.company_input.enter_text(text)

    def enter_first_line_address(self, text):
        self.first_address_input.enter_text(text)

    def enter_city(self, city):
        self.city_input.enter_text(city)

    def enter_postcode(self, postcode):
        self.postcode_input.enter_text(postcode)

    def enter_password(self, password):
        self.password_input.enter_text(password)

    def confirm_password(self, password):
        self.confirm_password_input.enter_text(password)

    def select_country(self, country):
        self.country_dropdown.select_by_text(country)

    def select_state(self, state):
        self.region_dropdown.select_by_text(state)

    def subscribe_to_newsletters(self):
        self.subscribe_btn.select()

    def unsubscribe_from_newsletters(self):
        self.unsubscribe_btn.select()

    def agree_to_privacy_policy(self):
        self.privacy_policy_checkbox.select()

    def submit_form(self):
        self.contniue_btn.submit()