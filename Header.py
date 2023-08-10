from Wrapper.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

class Header:
    def __init__(self, browser):
        self.my_account_btn = Element(browser, By.XPATH, "//a[@title='My Account']")
        self.my_acccount_dropdown = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")
        self.register_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
        self.login_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
        self.wish_list_btn = Element(browser, By.ID, "wishlist-total")
        self.shopping_list_btn = Element(browser, By.XPATH, "//a[@title='Shopping Cart']")
        self.checkout_btn = Element(browser, By.XPATH, "//a[@title='Checkout']")
        self.currency_btn = Element(browser, By.ID, "form-currency")
        self.currency_dropdown = Element(browser, By.XPATH, '//*[@id="form-currency"]/div/ul')
        self.currency_euro = Element(browser, By.NAME, 'EUR')
        self.currency_pound = Element(browser, By.NAME, "GBP")
        self.currency_dollar = Element(browser, By.NAME, 'USD')
        self.logo = Element(browser, By.ID, "logo")
        self.search = Element(browser, By.ID, "search")
        self.search_btn = Element(browser, By.XPATH, '//*[@id="search"]/span/button')

    def verify_logo_is_visible(self):
        return self.logo.wait_until_visible()

    def open_registration_form(self):
        self.my_account_btn.click()
        self.my_acccount_dropdown.wait_until_visible()
        self.register_btn.click()

    def open_login_page(self):
        self.my_account_btn.click()
        self.my_acccount_dropdown.wait_until_visible()
        self.login_btn.click()

    def change_currency_euro(self):
        self.currency_btn.click()
        self.currency_dropdown.wait_until_visible()
        self.currency_euro.click()

    def change_currency_pound(self):
        self.currency_btn.click()
        self.currency_dropdown.wait_until_visible()
        self.currency_pound.click()

    def change_currency_dollar(self):
        self.currency_btn.click()
        self.currency_dropdown.wait_until_visible()
        self.currency_dollar.click()

    def open_wishlist(self):
        self.wish_list_btn.click()

    def search_for(self, text):
        self.search = input(text)
        self.search_btn.click()


    def open_shopping_list(self):
        self.shopping_list_btn.click()

    def checkout(self):
        self.checkout_btn.click()