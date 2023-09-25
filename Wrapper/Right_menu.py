from Wrapper.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class RightMenu:
    def __init__(self, browser):
        self.login_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[1]")
        self.registration_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[2]")
        self.forgotten_password_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[3]")
        self.my_account_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[4]")
        self.address_book_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[5]')
        self.wish_list_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[6]')
        self.order_history_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[7]')
        self.downloads_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[8]')
        self.recurring_payments_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[9]')
        self.reward_points_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[10]')
        self.returns_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[11]')
        self.transactions_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[12]')
        self.newsletter_btn = Element(browser, By.XPATH, '//*[@id="column-right"]/div/a[13]')

    def click_login(self):
        self.login_btn.click()

    def click_registration(self):
        self.registration_btn.click()

    def click_forgotten_btn(self):
        self.forgotten_password_btn.click()

    def click_my_account(self):
       self.my_account_btn.click()

    def click_address_book_btn(self):
        self.address_book_btn.click()

    def click_wish_list_btn(self):
        self.wish_list_btn.click()

    def click_order_history_btn(self):
        self.order_history_btn.click()

    def click_downloads_btn(self):
        self.downloads_btn.click()

    def click_recurring_payments_btn(self):
        self.recurring_payments_btn.click()

    def click_reward_points_btn(self):
        self.reward_points_btn.click()

    def click_returns_btn(self):
        self.returns_btn.click()

    def click_transactions_btn(self):
        self.transactions_btn.click()

    def click_newsletter(self):
        self.newsletter_btn.click()
