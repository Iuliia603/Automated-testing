from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium import webdriver

# Установка переменной среды PATH для ChromeDriver
chromedriver_path = 'C:/chromedriver/'
os.environ['PATH'] = chromedriver_path + os.pathsep + os.environ['PATH']

class Browser:
    """
    This class is a wrapper around Selenium driver
    """
    def __init__(self, url, browser_name="chrome", time_wait=10):
        # Decide which browser to open based on browser_name parameter
        if browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=360")
            options.add_argument("--height=800")
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference("browser.urlbar.showPopup", True)
            self.driver = webdriver.Firefox(options=options)
            self.driver.maximize_window()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--window-size=360,800")
            options.add_argument("--incognito")
            options.add_argument("--disable-popup-blocking")
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
            self.driver = webdriver.Chrome(options=options)

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(time_wait)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()