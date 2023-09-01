from selenium.webdriver.common.by import By
from Wrapper.Browser import Browser
from Wrapper.UIElement import UIElement as Element
from Wrapper.HomePage import HomePage
import time

URL = 'https://cleveronly.com/brainbucket/'

def test_pcs():
    browser = Browser(URL)
    home_page = HomePage(browser)
    time.sleep(2)
    home_page.show_pcs()

    pcs = Element(browser, By.XPATH, "//div[contains(@class, 'product-layout product-grid')]")
    try:
        pcs_elements = pcs.get_elements()
    except:
        no_product_message = Element(browser, By.XPATH, '//*[@id="content"]/p')
        assert "There are no products to list in this category." == no_product_message

    assert len(pcs_elements()) == 1

    time.sleep(2)
    browser.shutdown()

def test_macs():
    browser = Browser(URL)
    home_page = HomePage(browser)
    time.sleep(2)
    home_page.show_mac_laptops()

    macs = Element(browser, By.XPATH, "//div[contains(@class, 'product-layout product-grid')]")
    try:
        macs_elements = macs.get_elements()
    except:
        no_product_message = Element(browser, By.XPATH, '//*[@id="content"]/p')
        assert "There are no products to list in this category." == no_product_message

    assert len(macs_elements()) == 1
    time.sleep(2)
    browser.shutdown()

if __name__ == "__main__":
    test_pcs()
    test_macs()