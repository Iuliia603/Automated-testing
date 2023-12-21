from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.homepage_title = Element(browser, By.XPATH, '//*[@id="chips"]')
        self.search_fild = Element(browser, By.XPATH, "//input[@id='search' and @placeholder='Введите запрос']")
        self.search_fild_btn = Element(browser, By.XPATH, '//*[@id="sb_ifc50"]')
        self.search_btn = Element(browser, By.ID, 'search-icon-legacy')

    def get_homepage_title(self):
        return self.homepage_title.get_text()

    def click_search_field(self):
        self.search_fild.click()

    def input_request(self, text):
        self.search_fild.enter_text(text)

    # def input_request(self, text):
    #     self.search_fild.enter_text(text)

    def enter_request(self):
        self.search_btn.click()

