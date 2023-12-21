from Test_Tasks.Wrapper_YouTube.Home_Page import HomePage
from Test_Tasks.Wrapper_YouTube.Search_result import SearchPage
from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

class VideoPlayer:
    def __init__(self, browser):
        self.browser = browser
        self.homepage = HomePage(browser)
        self.search_page = SearchPage(browser)
        self.player = Element(By.CLASS_NAME, "html5-video-player")
        self.mini_player = Element(browser, By.XPATH, '//*[@id="movie_player"]/div[36]/div[2]/div[2]/button[5]')

    def click_mini_player(self):
        self.mini_player.click()





