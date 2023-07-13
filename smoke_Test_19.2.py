from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

service = Service(executable_path='C:/chromedriver/chromedriver')
driver = webdriver.Chrome(service=service)


driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver.maximize_window()  #m aximizing the browser window

#07/12 Julia
wd_wait = WebDriverWait(driver, 10)
logo = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@title='Brainbucket']")))

Login = driver.find_element(by=By.NAME, value="email")
Login.clear()
Login.send_keys("iuliia60358@gmail.com")

Password = driver.find_element(by=By.NAME, value="password")
Password.clear()
Password.send_keys("123456Z")

# 07/12 Julia
login_bth = wd_wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/div[2]/div/form/input")))
login_bth.click()

#getting the background color of the button
new_registrant_btn = wd_wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))
background_color = new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
new_registrant_btn.click()

wd_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h1')))

#Register Account
#driver.find_element()
#Personal Details

firstname_input = driver.find_element(by=By.NAME, value="firstname")
firstname_input.clear()
firstname_input.send_keys("Lana")

last_name = driver.find_element(by=By.NAME, value='lastname')
last_name.clear()
last_name.send_keys("Kartashova")

email = driver.find_element(by=By.NAME, value='email')
email.clear()
email.send_keys('iuliia60358@gmail.com')

telephone = driver.find_element(by=By.NAME, value='telephone')
telephone.clear()
telephone.send_keys('89764235891')

address_1 = driver.find_element(by=By.NAME, value='address_1')
address_1.clear()
address_1.send_keys('657 PA')

city = driver.find_element(by=By.NAME, value='city')
city.clear()
city.send_keys('Pittsburgh')

#07/12 Julia
country_dropdown = driver.find_element(by=By.ID, value="input-country")
country_dropdown_select = Select(country_dropdown)
country_dropdown_select.select_by_value("223")
#07/12 Julia
region_dropdown = driver.find_element(by=By.ID, value="input-zone")
region_dropdown_select = Select(region_dropdown)
region_dropdown_select.select_by_visible_text("Pennsylvania")

password_reg = driver.find_element(by=By.NAME, value='password')
password_reg.clear()
password_reg.send_keys('123456Z')

password_confirm = driver.find_element(by=By.NAME, value='confirm')
password_confirm.clear()
password_confirm.send_keys('123456Z')

firstname_field = driver.find_element(by=By.XPATH, value="//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

last_name_field = driver.find_element(by=By.XPATH, value='//*[@id="account"]/div[3]')
last_name_field_class = last_name_field.get_attribute('class')
assert 'required' in last_name_field_class

email_field = driver.find_element(by=By.XPATH, value='//*[@id="account"]/div[4]')
email_field_class = email_field.get_attribute('class')
assert 'required' in email_field_class

telephone_field = driver.find_element(by=By.XPATH, value='//*[@id="account"]/div[5]')
telephone_field_class = telephone_field.get_attribute('class')
assert 'required' in telephone_field_class

address_1_field = driver.find_element(by=By.XPATH, value='//*[@id="address"]/div[2]')
address_1_field_class = address_1_field.get_attribute('class')
assert 'required' in address_1_field_class

city_flied = driver.find_element(by=By.XPATH, value='//*[@id="address"]/div[4]')
city_flied_class = city_flied.get_attribute('class')
assert 'required' in city_flied_class

password_reg_flied = driver.find_element(by=By.XPATH, value='//*[@id="content"]/form/fieldset[3]/div[1]')
password_reg_flied_class = password_reg_flied.get_attribute('class')
assert 'required' in password_reg_flied_class

password_confirm_flied = driver.find_element(by=By.XPATH, value='//*[@id="content"]/form/fieldset[3]/div[2]')
password_confirm_class = password_confirm_flied.get_attribute('class')
assert 'required' in password_confirm_class

#07/12 Julia
subscribe_r_btn = driver.find_element(by=By.XPATH, value='//*[@id="content"]/form/fieldset[4]/div/div/label[2]')
if not subscribe_r_btn.is_selected():
    subscribe_r_btn.click()
#07/12 Julia
privacy_cb = driver.find_element(by=By.NAME, value="agree")
if not privacy_cb.is_selected():
    privacy_cb.click()

continue_registrant_btn = wd_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/form/div/div/input[2]')))
continue_background_color = continue_registrant_btn.value_of_css_property('background-color')
converted_continue_background_color = Color.from_string(continue_background_color)
assert converted_continue_background_color.rgb == 'rgb(34, 154, 200)'


time.sleep(10)
driver.quit()