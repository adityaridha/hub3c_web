import sys
import os
import pytest
import time
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)

from page_model import Registration
from page_model import Registration_Existing_Membership
from connection import Connection
from faker import Factory


driver = Connection.driver
regis = Registration(driver)
regis_exist = Registration_Existing_Membership(driver)

class TestRegistrationExistingMembership():

    fake = Factory.create()
    first_name = "Auto"
    last_name = fake.first_name()
    last_name2 = fake.first_name()
    company_name = "Auto " + last_name
    company_name2 = "Auto " + last_name2
    email = "automation.hub1@mailinator.com"
    password = "ZXasqw12"

    #1  Login using registered email & correct password
    def test_login_success(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.input_email_address(self.email)
        regis_exist.input_password(self.password)
        regis_exist.click_login()
        regis_exist.is_directed_to_registration_page()

    #2  Login using registered email & wrong password
    def test_login_fail(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.input_email_address(self.email)
        regis_exist.input_password("ZXasqw")
        regis_exist.click_login()
        regis_exist.is_login_fail()

    #3  Login using registered email & wrong password, >1 attempts
    def test_login_success_after_failed(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.input_email_address(self.email)
        regis_exist.input_password("ZXasqw")
        regis_exist.click_login()
        regis_exist.is_login_fail()
        regis_exist.input_password("ZXasqwqw")
        regis_exist.click_login()
        regis_exist.is_login_fail()
        regis_exist.input_password("ZXasqwqwqw")
        regis_exist.click_login()
        regis_exist.is_login_fail()
        regis_exist.input_password(self.password)
        regis_exist.click_login()
        regis_exist.is_directed_to_registration_page()

    #4  Login using unregistered email
    def test_login_unregistered_email(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.input_email_address("automation.hub999@mailinator.com")
        regis_exist.input_password(self.password)
        regis_exist.click_login()
        regis_exist.is_login_fail()

    #5  Login using incorrect email format
    def test_login_invalid_email_address(self):
        #without @
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.input_email_address("automation.hub999mailinator.com")
        regis_exist.input_password(self.password)
        regis_exist.click_login()
        regis_exist.is_login_fail()

        time.sleep(2)
        #without dot (.) after @
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.input_email_address("automation.hub999@mailinator")
        regis_exist.input_password(self.password)
        regis_exist.click_login()
        regis_exist.is_login_fail()

    #6  Login without filling email field
    def test_login_unregistered_email(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.input_password(self.password)
        regis_exist.click_login()
        regis_exist.is_login_fail()

    #7  Login without filling password field
    def test_login_unregistered_email(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.input_email_address(self.email)
        regis_exist.click_login()
        regis_exist.is_login_fail()

    #8  Login without filling email & password field
    def test_login_unregistered_email(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis_exist.click_login()
        regis_exist.is_login_fail()

    #9  Register by inputting all fields
    def test_registration(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        self.test_login_success()

        regis.input_company_name(self.company_name)
        regis.select_salutation()
        regis.tick_tnc()
        regis.create_account()
        regis.is_registration_success()

    #10 Register by inputting all mandatory field (w/o "Salutation")
    def test_registration_mandatory_only(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        self.test_login_success()

        regis.input_company_name(self.company_name2)
        regis_exist.select_salutation()
        regis.tick_tnc()
        regis.create_account()
        regis.is_registration_success()
