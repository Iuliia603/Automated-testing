from behave import *
from Wrapper.Login_page import LoginPage
from Wrapper.Registrant_page import RegistrationPage

"""
Given user on the registration page
    When user types "<value>" in "<field>"
    And user clicks Contunue button
    Then error is shown under "<field>" field
    """

@given("user on the registration page")
def open_registration_page(context):
    login_page = LoginPage(context.browser)
    login_page.click_continue_btn()


@when('user types "{value}" in "{field}"')
def type_value_in_field(context, value, field):
    registration_page = RegistrationPage(context.browser)
    context.registration_form = registration_page

    if value == "None":
        return

    if field == "first_name":
        registration_page.enter_first_name(value)
    elif field == "last_name":
        registration_page.enter_last_name(value)
    elif field == "phonenumber":
        registration_page.enter_telephone(value)
    elif field == "password":
        registration_page.enter_password(value)
    elif field == "email":
        registration_page.enter_email(value)
    elif field == "city":
        registration_page.enter_city(value)
    elif field == "address-1":
        registration_page.enter_first_line_address(value)


@when("user clicks Continue button")
def submit_on_registration_form(context):
    context.registration_form.submit_form()

@then('error is shown under "{field}" field')
def verify_error_registration_form(context, field):
    context.browser.get_wd_wait()
    if field == "first_name":
        assert context.registration_form.get_firstname_error() == "First Name must be between 1 and 32 characters!"
    elif field == "last_name":
        assert context.registration_form.get_lastname_error() == "Last Name must be between 1 and 32 characters!"
    elif field == "phonenumber":
        assert context.registration_form.get_phonenumber_error() == "Telephone must be between 3 and 32 characters!"
    elif field == "password":
        assert context.registration_form.get_password_error() == "Password must be between 4 and 20 characters!"
    elif field == "email":
        assert context.registration_form.get_email_error() == "E-Mail Address does not appear to be valid!"
    elif field == "address_1":
        assert context.registration_form.get_address_error() == "Address 1 must be between 3 and 128 characters!"
    elif field == "city":
        assert context.registration_form.get_city_error() == "City must be between 2 and 128 characters!"
