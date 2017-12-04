import sys
import os
import pytest
import time
from pathlib import Path
root = Path(__file__).parents[2]   #get the root directory
root_model = str(root)
sys.path.append(root_model)

import page_model
from connection import Connection

driver = Connection.driver
login = page_model.Login(driver)

class TestLogin():

    email = "marsha@freehub.com"
    password = "ZXasqw12"

    #1  test_login using registered email & correct password
    def test_login_success(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email_address(self.email)
        login.input_password(self.password)
        login.click_login()
        login.is_login_success()
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/SignOut")

    #2  test_login using registered email & wrong password
    def test_login_fail(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email_address(self.email)
        login.input_password("ZXasqw")
        login.click_login()
        login.is_login_fail()

    #3  test_login using registered email & correct password, after login failed with >1 attempts
    def test_login_success_after_failed(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email_address(self.email)
        login.input_password("ZXasqw")
        login.click_login()
        login.is_login_fail()
        login.input_password("ZXasqwqw")
        login.click_login()
        login.is_login_fail()
        login.input_password("ZXasqwqwqw")
        login.click_login()
        login.is_login_fail()
        login.input_password(self.password)
        login.click_login()
        login.is_login_success()
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/SignOut")

    #4  test_login using unregistered email
    def test_login_unregistered_email(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email_address("automation.hub999@mailinator.com")
        login.input_password(self.password)
        login.click_login()
        login.is_login_fail()

    #5  test_login using incorrect email format
    def test_login_invalid_email_address(self):
        #without @
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email_address("automation.hub999mailinator.com")
        login.input_password(self.password)
        login.click_login()
        login.is_login_fail()

        time.sleep(2)
        #without dot (.) after @
        driver.get("https://test-z5y5zwrh0g.hub3c.com")
        login.input_email_address("automation.hub999@mailinator")
        login.input_password(self.password)
        login.click_login()
        login.is_login_fail()

    #6  test_login without filling email field
    def test_login_email_address_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com")
        login.input_password(self.password)
        login.click_login()
        login.is_email_address_empty()

    #7  test_login without filling password field
    def test_login_password_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com")
        login.input_email_address(self.email)
        login.click_login()
        login.is_password_empty()

    #8  test_login without filling email & password field
    def test_login_mandatory_fields_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com")
        login.click_login()
        login.is_email_address_empty()
        login.is_password_empty()

    #9  Click on registration link
    def test_registration_link(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com")
        login.go_to_registration()
        login.is_directed_to_registration_page()

    #10 Click on forgot password link
    def test_forgot_password_link(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com")
        login.go_to_forgot_password()
        login.is_directed_to_forgot_password_page()




