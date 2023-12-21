from Test_Tasks.Wrapper_YouTube.Home_Page import HomePage
from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, browser):
        self.browser = browser
        self.homepage = HomePage(browser)

        self.search_title = Element(browser, By.XPATH,'//*[@id="text"]')
        self.name_video = Element(browser, By.XPATH, '//*[@id="video-title"]/yt-formatted-string')

    def get_search_title(self):
        return self.search_title.get_text()

    def get_name_video_title(self):
        return self.name_video.get_text()

    def click_video(self):
        self.name_video.click()




