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
forgot_password = page_model.Forgot(driver)

class TestForgotPassword():

    email = "marsha@freehub.com"

    #1 test_reset using registered & correct email
    def test_forgot_password_success(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/RecoverPassword")
        forgot_password.input_email_address(self.email)
        forgot_password.click_reset()
        forgot_password.is_reset_success()

    #2 test_reset using unregistered email
    def test_forgot_password_fail(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/RecoverPassword")
        forgot_password.input_email_address("testingggemail@mailinator.com")
        forgot_password.click_reset()
        forgot_password.is_reset_fail()

    #3 test_reset using incorrect email format
    def test_forgot_password_incorrect(self):
        # without @
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/RecoverPassword")
        forgot_password.input_email_address("automation.hub999mailinator.com")
        forgot_password.click_reset()
        forgot_password.is_email_address_invalid()

        # without .
        time.sleep(2)
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/RecoverPassword")
        forgot_password.input_email_address("automation.hub999@mailinatorcom")
        forgot_password.click_reset()
        forgot_password.is_email_address_invalid()