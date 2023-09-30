from selenium.webdriver.common.by import By
from Wrapper.UIElement import UIElement as Element
from Wrapper.Header import Header
from Wrapper.Right_menu import RightMenu
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
   def __init__(self, browser):
       self.header = Header(browser)
       # Menu Options
       self.right_menu = RightMenu(browser)

       self.my_account_title = Element(browser, By.XPATH, "//h2[contains(text(), 'My Account')]")
       self.edit_your_acct_info_link = Element(browser, By.XPATH, "//a[contains(text(), 'Edit your account')]")
       self.change_password_link = Element(browser, By.XPATH, "a//[contains(text(), 'Edit your password')]")
       self.modify_address_book_link = Element(browser, By.XPATH, "//a[contains(text(), 'Modify your address')]")
       self.modify_wishlist = Element(browser, By.XPATH, "//a[contains(text(), 'Modify your wish list')]")

       self.my_orders_title = Element(browser, By.XPATH, "//h2[contains(text(), 'My Orders')]")
       self.view_order_history_link = Element(browser, By.XPATH, "//a[contains(text(), 'View your order history')]")
       self.downloads_link = Element(browser, By.XPATH, "a//[contains(text(), 'Downloads')]")
       self.reward_points_link = Element(browser, By.XPATH, "//a[contains(text(), 'Your Reward Points')]")
       self.return_request_link = Element(browser, By.XPATH, "//a[contains(text(), 'View your return requests')]")
       self.transactions_link = Element(browser, By.XPATH, "//a[contains(text(), 'Your Transactions')]")
       self.recurring_payments_link = Element(browser, By.XPATH, "//a[contains(text(), 'Recurring payments')]")

       self.newsletter_title = Element(browser, By.XPATH, "//h2[contains(text(), 'Newsletter')]")
       self.subscribe_link = Element(browser, By.XPATH, "//a[contains(text(), 'unsubscribe to newsletter')]")

   def get_my_account_title(self):
       return self.my_account_title.get_text()

   def get_my_orders_title(self):
       return self.my_orders_title.get_text()

   def get_newsletter_title(self):
       return self.newsletter_title.get_text()

   def wait_for_profile_page_to_load(self, wait):
       wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'My Account')]")))
       wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'My Orders')]")))
       wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Newsletter')]")))