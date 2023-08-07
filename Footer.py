from selenium.webdriver.common.by import By
from Wrapper.Browser import Browser
from Wrapper.UIElement import UIElement as Element


class Footer:
    def __init__(self, browser):
        self.about_us = Element(browser, By.XPATH, "/html/body/footer/div/div/div[1]/ul/li[1]/a")
        self.delivery_info = Element(browser, By.XPATH, "/html/body/footer/div/div/div[1]/ul/li[2]/a")
        self.privacy = Element(browser, By.XPATH, "/html/body/footer/div/div/div[1]/ul/li[3]/a")
        self.terms = Element(browser, By.XPATH, "/html/body/footer/div/div/div[1]/ul/li[4]/a")
        self.contact_us = Element(browser, By.XPATH, "/html/body/footer/div/div/div[2]/ul/li[1]/a")
        self.returns = Element(browser, By.XPATH, "/html/body/footer/div/div/div[2]/ul/li[2]/a")
        self.site_map = Element(browser, By.XPATH, "/html/body/footer/div/div/div[2]/ul/li[3]/a")
        self.brands = Element(browser, By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[1]/a")
        self.gift = Element(browser, By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[2]/a")
        self.affiliates = Element(browser, By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[3]/a")
        self.specials = Element(browser, By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[4]/a")
        self.my_account = Element(browser, By.XPATH, "/html/body/footer/div/div/div[4]/ul/li[1]/a")
        self.order_history = Element(browser, By.XPATH, "/html/body/footer/div/div/div[4]/ul/li[2]/a")
        self.wish_list = Element(browser, By.XPATH, "/html/body/footer/div/div/div[4]/ul/li[3]/a")
        self.newsletter = Element(browser, By.XPATH, "/html/body/footer/div/div/div[4]/ul/li[4]/a")

    def click_about_us(self):
        self.about_us.click()
    def click_delivery_info(self):
        self.delivery_info.click()
    def click_privacy(self):
        self.privacy.click()
    def click_terms(self):
        self.terms.click()
    def click_contact_us(self):
        self.contact_us.click()
    def click_returns(self):
        self.returns.click()
    def click_site_map(self):
        self.site_map.click()
    def click_brands(self):
        self.brands.click()
    def click_gift(self):
        self.gift.click()
    def click_affiliates(self):
        self.affiliates.click()
    def click_specials(self):
        self.specials.click()
    def click_my_account(self):
        self.my_account.click()
    def click_order_history(self):
        self.order_history.click()
    def click_wish_list(self):
        self.wish_list.click()
    def click_newletter(self):
        self.newsletter.click()

