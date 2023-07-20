from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
# Julia 07/19
from Wrapper.Browser import Browser
from Wrapper.UIElement import UIElement as Element
from Wrapper.Dropdown import Dropdown
# Julia 07/19
browser = Browser("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver = browser.get_driver()

# Julia 07/19
logo = Element(browser, By.XPATH, "//img[@title='Brainbucket']")

Login = driver.find_element(by=By.NAME, value="email")
Login.clear()
Login.send_keys("iuliia60358@gmail.com")

Password = driver.find_element(by=By.NAME, value="password")
Password.clear()
Password.send_keys("123456Z")

# 07/12 Julia
login_bth = Element(browser, By.XPATH, "//*[@id='content']/div/div[2]/div/form/input")
login_bth.click()

## Julia 07/19
new_registrant_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
new_registrant_btn.click()

## Julia 07/19
Element(browser, By.XPATH, '//*[@id="content"]/h1').wait_until_visible()
inputs = {
    "firstname": "Julia",
    "lastname": "Kartashova",
    "email": 'iuliia60358@gmail.com',
    "telephone": "89764235891",
    "address_1": "675 PA",
    "city": "Pittsburgh",
    "password": "78456Z",
    "confirm": "78456Z"
}
for field, text in inputs.items():
    input_field = Element(browser, By.NAME, field)
    input_field.enter_text(text)

# Julia 07/19 - 2
Dropdown(browser, By.ID, "input-country").select_by_value("223")

# Julia 07/19 - 2
Dropdown(browser, By.ID, "input-zone").select_by_text("Pennsylvania")

#Julia 07/19
subscribe_r_btn = driver.find_element(by=By.XPATH, value='//*[@id="content"]/form/fieldset[4]/div/div/label[2]')
if not subscribe_r_btn.is_selected():
    subscribe_r_btn.click()
privacy_cb = driver.find_element(by=By.NAME, value="agree")
if not privacy_cb.is_selected():
    privacy_cb.click()

time.sleep(10)
# Julia 07/19
browser.shutdown()