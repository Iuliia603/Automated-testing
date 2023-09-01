from selenium.webdriver.common.by import By
from Wrapper.Browser import Browser
from Wrapper.UIElement import UIElement as Element
from Wrapper.HomePage import HomePage
import time

URL = 'https://cleveronly.com/brainbucket/'

def test_opening_all_desktops():
    browser = Browser(URL)
    home_page = HomePage(browser)
    time.sleep(2)
    home_page.show_all_desktops()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Desktops"

    time.sleep(2)
    browser.shutdown()

def test_show_pcs():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_pcs()

    section_title_pc = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title_pc == "PC"

    time.sleep(2)
    browser.shutdown()

def test_show_mac_desktops():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_mac_desktops()

    section_title_mac = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title_mac == "Mac"

    time.sleep(2)
    browser.shutdown()


def test_show_all_laptops():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_all_laptops()

    section_title_all_lap = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title_all_lap == "Laptops & Notebooks"

    time.sleep(2)
    browser.shutdown()

def test_show_mac_laptops():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_mac_laptops()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Macs"

    time.sleep(2)
    browser.shutdown()

def test_show_windows_laptops():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_windows_laptops()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Windows"

    time.sleep(2)
    browser.shutdown()

def test_show_all_components():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_all_components()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == 'Components'

    time.sleep(2)
    browser.shutdown()

def test_show_mice():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_mice()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == 'Mice and Trackballs'

    time.sleep(2)
    browser.shutdown()

def test_show_monitors():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_monitors()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Monitors"

    time.sleep(2)
    browser.shutdown()

def test_show_printers():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_printers()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Printers"

    time.sleep(2)
    browser.shutdown()

def test_show_scanners():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_scanners()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Scanners"

    time.sleep(2)
    browser.shutdown()

def test_show_web_cameras():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_web_cameras()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Web Cameras"

    time.sleep(2)
    browser.shutdown()

def test_show_all_phones_and_pdas():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_all_phones_and_pdas()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Phones & PDAs"

    time.sleep(2)
    browser.shutdown()

def test_show_pdas():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_pdas()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "PDAs"

    time.sleep(2)
    browser.shutdown()

def test_show_phones():
    browser = Browser(URL)
    time.sleep(2)
    home_page = HomePage(browser)
    home_page.show_phones()

    section_title = Element(browser, By.XPATH, '//*[@id="content"]/h2').get_text()
    assert section_title == "Phones"

    time.sleep(2)
    browser.shutdown()

if __name__ == "__main__":
    test_opening_all_desktops()
    test_show_pcs()
    test_show_mac_desktops()
    test_show_all_laptops()
    test_show_mac_laptops()
    test_show_windows_laptops()
    test_show_all_components()
    test_show_mice()
    test_show_monitors()
    test_show_printers()
    test_show_scanners()
    test_show_web_cameras()
    test_show_all_phones_and_pdas()
    test_show_pdas()
    test_show_phones()