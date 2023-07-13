from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:/chromedriver/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver.maximize_window()

#logo = driver.find_element(by=By.XPATH, value="//img[@title='Brainbucket']")
# 07.12 Julia
wd_wait = WebDriverWait(driver, 10)
logo = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@title='Brainbucket']")))

#new_registrant_btn = driver.find_element(by=By.XPATH, value="//a[contains(text(), 'Continue')]")
# 07.12 Julia
new_registrant_btn = wd_wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))
new_registrant_btn.click()

# explicit wait “Register Account”
# 07.12 Julia
wd_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h1')))

firstname_input = driver.find_element(by=By.NAME, value="firstname")
firstname_input.clear()
firstname_input.send_keys("Lana")

firstname_field = driver.find_element(by=By.XPATH, value="//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

#continue_registrant_btn = driver.find_element(by=By.XPATH, value='//*[@id="content"]/form/div/div/input[2]')
# 07.12 Julia
continue_registrant_btn = wd_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/form/div/div/input[2]')))
time.sleep(10)
driver.quit()