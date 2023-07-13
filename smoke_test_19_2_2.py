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
wd_wait = WebDriverWait(driver, 10)

my_account_dd = driver.find_element(by=By.XPATH, value='//*[@id="top-links"]/ul/li[2]/a')
my_account_dd.click()

login_option = wd_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')))
login_option.click()
wd_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div/h2')))

my_account_dd2 = driver.find_element(by=By.XPATH, value='//*[@id="top-links"]/ul/li[2]/a/span[1]')
my_account_dd2.click()

register_option = wd_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')))
register_option.click()
wd_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h1')))

time.sleep(6)
driver.quit()
