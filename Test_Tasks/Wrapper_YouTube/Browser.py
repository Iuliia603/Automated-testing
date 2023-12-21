from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import undetected_chromedriver as uc
from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
import time


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
        elif browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("--start-maximized")
            options.add_argument("--window-size=360,800")
#            options.add_argument("--incognito")
            options.add_argument("--disable-popup-blocking")
            options.add_experimental_option("excludeSwitches", ['enable-automation'])

#            self.driver = webdriver.Chrome(options=options)
            self.driver = uc.Chrome()
            #driver.get("https://chykalophia.com/")
        elif browser_name.lower() == 'remote':
            desired_capabilities = {
                'browserName': 'chrome'}
            self.driver = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor="http://localhost:4444/wd/hub")
            # BROWSERSTACK_URL = 'http://iuliia_SmZ2tQ:CvFJVNpvrHde4BdncjDT@hub-cloud.browserstack.com/wd/hub'
            #
            # desired_cap = {
            #     'os': 'Windows',
            #     'os_version': '10',
            #     'browserName': 'Chrome',
            #     'browserVersion': '80.0',
            #     'name': 'my second test'
            # }
            # self.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)


        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(time_wait)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)


#behave -f allure_behave.formatter:AllureFormatter -o path/to/allure/reports /Users/iuliia603/PycharmProjects/pythonProject/Test_Tasks/Youtube_Test/youtube_test.feature
