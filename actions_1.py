import time
from selenium.webdriver.common.by import By
from Wrapper.Browser import Browser
from Wrapper.UIElement import UIElement as Element
from Actions22.actions_пример import Actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://cleveronly.com/practice"
browser = Browser(URL)
driver = browser.get_driver()
actions = Actions(browser)


double_field = Element(browser, By.XPATH, '//*[@id="card"]')
keydown_field = Element(browser, By.XPATH, '//*[@id="key_practice"]/input')
context_menu = Element(browser, By.XPATH, '//*[@id="context_menu"]')
logo = Element(browser, By.XPATH, '//*[@id="drag1"]')
drop_logo = Element(browser, By.XPATH, '//*[@id="droplogo123"]')
change_color = Element(browser, By.XPATH, '/html/body/div/ul/li[1]')
change_font = Element(browser, By.XPATH, '/html/body/div/ul/li[2]')
open_tsa = Element(browser, By.XPATH, '/html/body/div/ul/li[3]/a')

#1
initial_color = double_field.get_element().value_of_css_property("background-color")
print("Initial color is", initial_color)

actions = Actions(browser)
actions.double_click(double_field)

time.sleep(2)

new_color = double_field.get_element().value_of_css_property("background-color")
print("New color", new_color)
if initial_color != new_color:
    print("Color changed")
else:
    print("Color is not changed")

#2
actions.send_keys_to_element(keydown_field, Keys.ENTER)

wd_wait = WebDriverWait(driver, 10)
wd_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="hidden_text"]')))

# 3
initial_background_color = context_menu.get_element().value_of_css_property("background-color")
print("Initial background color is", initial_background_color)

actions.right_click(context_menu)
actions.click(change_color)

time.sleep(4)

new_background_color = context_menu.get_element().value_of_css_property("background-color")
print("New background color", new_background_color)
if initial_background_color != new_background_color:
    print("Background color changed")
else:
    print("Background color is not changed")

initial_style = context_menu.get_attribute("style")
print("Style ", initial_style)

actions.right_click(context_menu)
actions.click(change_font)

time.sleep(4)

new_style = context_menu.get_attribute("style")
print("New style ", new_style)
if "font-weight: bold" in new_style:
    print("Text is bold.")
else:
    print("Text is not bold.")


actions.right_click(context_menu)
actions.key_down(Keys.ESCAPE)
actions.key_up(Keys.ESCAPE)

time.sleep(4)

# 4
actions = Actions(browser)
actions.drag_and_drop(logo, drop_logo)

# 3
actions.right_click(context_menu)
actions.click(open_tsa)

time.sleep(4)
browser.shutdown()
