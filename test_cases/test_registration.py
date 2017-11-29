import sys
import os
import pytest
import time
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)

from page_model import Registration
from connection import Connection
from faker import Factory


driver = Connection.driver
regis = Registration(driver)

URL_TEST = "https://test-z5y5zwrh0g.hub3c.com/Join/Index"

class TestRegistration():

    fake = Factory.create()
    first_name = "Auto"
    last_name = fake.first_name()
    last_name2 = fake.first_name()
    company_name = "Auto " + last_name
    company_name2 = "Auto " + last_name2
    email = "auto." + last_name + "@mailinator.com"
    email2 = "auto." + last_name2 + "@mailinator.com"
    password = "ZXasqw12"

    #1  Register by inputting all fields
    def test_registration(self):
        driver.get(URL_TEST)
        regis.input_company_name(self.company_name)
        regis.select_salutation()
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_registration_success()

    #2  Register by inputting all mandatory fields (w/o "Salutation")
    def test_registration_mandatory_only(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name2)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name2)
        regis.input_email_address(self.email2)
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_registration_success()

    #3  Register using existing Company name
    def test_registration_existing_company_name(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name("Hub3c")
        regis.input_first_name("Auto")
        regis.input_last_name("Hub999")
        regis.input_email_address("automation.hub999@mailinator.com")
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_company_name_exist()

    #4  Register using existing email address
    def test_registration_existing_email_address(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name("Automation-Hub999")
        regis.input_first_name("Auto")
        regis.input_last_name("Hub999")
        regis.input_email_address("mike@hub3c.com")
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_email_address_exist()

    #5  Register by emptying all mandatory fields
    def test_registration_all_mandatory_fields_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.tick_tnc()
        regis.create_account()
        regis.is_company_name_empty()
        regis.is_first_name_empty()
        regis.is_last_name_empty()
        regis.is_email_address_empty()
        regis.is_password_empty()
        regis.is_repeat_password_empty()

    #6  Register by emptying only "Company Name"
    def test_registration_company_name_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_company_name_empty()

    #7  Register by emptying only "First Name"
    def test_registration_first_name_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_first_name_empty()

    #8  Register by emptying only "Last Name"
    def test_registration_last_name_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_email_address(self.email)
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_last_name_empty()

    #9  Register by emptying only "Email"
    def test_registration_email_address_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_email_address_empty()

    #10 Register by emptying only "Password"
    def test_registration_password_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_password_empty()

    #11 Register by emptying only "Repeat Password"
    def test_registration_repeat_password_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_repeat_password_empty()

    #12 Register by inputting unmatched password
    def test_registration_unmatched_password(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password(self.password)
        regis.input_repeat_password("ZXasqw123")
        regis.tick_tnc()
        regis.create_account()
        regis.is_password_unmatched()

    #13 Register by inputting invalid password: 6 chars, without one uppercase letter
    def test_registration_password_without_uppercase(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password("zxas12")
        regis.input_repeat_password("zxas12")
        regis.tick_tnc()
        regis.create_account()
        regis.is_password_invalid()

    #14 Register by inputting invalid password: 6 chars, without one lowercast letter
    def test_registration_password_without_lowercase(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password("ZXAS12")
        regis.input_repeat_password("ZXAS12")
        regis.tick_tnc()
        regis.create_account()
        regis.is_password_invalid()

    #15 Register by inputting invalid password: 6 chars, without one number
    def test_registration_password_without_number(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password("ZXASQW")
        regis.input_repeat_password("ZXASQW")
        regis.tick_tnc()
        regis.create_account()
        regis.is_password_invalid()

    #16 Register by inputting invalid password: <6 chars
    def test_registration_password_less_than_six(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address(self.email)
        regis.input_password("ZXas1")
        regis.input_repeat_password("ZXas1")
        regis.tick_tnc()
        regis.create_account()
        regis.is_password_invalid()

    #17 Register by inputting incorrect email format
    def test_registration_invalid_email_address(self):
        #without @
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address("automation.hub999mailinator.com")
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_email_address_invalid()

        time.sleep(2)
        #without dot (.) after @
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name(self.company_name)
        regis.input_first_name(self.first_name)
        regis.input_last_name(self.last_name)
        regis.input_email_address("automation.hub999@mailinator")
        regis.input_password(self.password)
        regis.input_repeat_password(self.password)
        regis.tick_tnc()
        regis.create_account()
        regis.is_email_address_invalid()
