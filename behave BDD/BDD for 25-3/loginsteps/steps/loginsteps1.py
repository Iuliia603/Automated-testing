from behave import given, when, then
# from Wrapper.Browser import Browser
from Wrapper.Login_page import LoginPage
from Wrapper.ProfilePage import ProfilePage
# from config.config_reader import ConfigReader
# import os

# URL = "https://cleveronly.com/brainbucket/index.php?route=account/login"
# file_path = os.path.join("behave_BDD/loginsteps/steps/config.ini")
# configs = ConfigReader(file_path)
# user1_email = configs.get_user1_email()
# user1_password = configs.get_user1_password()
#
# @given("user launch login page")
# def launch_login_page(context):
#     browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
#     context.browser = browser

@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page


@when("user enters correct email and password")
def enter_email_and_password(context):
    login_page = context.login_page
    configs = context.configs
    login_page.password_input(configs.get_user1_password())
    login_page.email_input(configs.get_user1_email())


@when('user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.login_btn_click()


@then("user profile is launched")
def verify_user_profile_view(context):
    profile_page = ProfilePage(context.browser)
    wait = context.browser.get_wd_wait()
    profile_page.wait_for_profile_page_to_load(wait)
    assert profile_page.get_my_account_title() == "My Account"
    assert profile_page.get_my_orders_title() == "My Orders"
    assert profile_page.get_newsletter_title() == "Newsletter"

@then("warning shown about 'No match for E-Mail Address and/or Password'")
def check_login_error_warning(context):
    login_page = context.login_page
    assert login_page.check_login_error_warning() == "Warning: No match for E-Mail Address and/or Password."

@when("user enters correct Email")
def user_enters_correct_email(context):
    login_page = context.login_page
    configs = context.configs
    login_page.email_input(configs.get_user1_email())

@when("user enters correct Email and incorrect Password")
def user_enters_email_and_incorrect_password(context):
    login_page = context.login_page
    configs = context.configs
    login_page.email_input(configs.get_user1_email())
    login_page.password_input(configs.get_user2_password())

@when("user enters incorrect Email and correct Password")
def user_enters_incorrect_email_and_correct_password(context):
    login_page = context.login_page
    configs = context.configs
    login_page.email_input(configs.get_user2_email())
    login_page.password_input(configs.get_user1_password())


