"""Scenario Outline: User can't login without entering <field>
  Given user is not logged in
  When user enters "<value>" in "<field>"
  And user clicks Login button
  Then warning is shown No match for E-Mail Address and/or Password
"""

from behave import given, when, then
from Wrapper.Login_page import LoginPage


@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page

@when('user enters "{value}" in "{field}"')
def enter_value_in_field(context, value, field):
    login_page = context.login_page

    if value == "None":
        return

    if field == "email":
        login_page.email_input(value)
    elif field == "password":
        login_page.password_input(value)

@when('user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.login_btn_click()

@then("warning is shown No match for E-Mail Address and/or Password")
def check_login_error_warning(context):
    login_page = context.login_page
    assert login_page.check_login_error_warning() == "Warning: No match for E-Mail Address and/or Password."

