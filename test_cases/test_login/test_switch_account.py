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

class TestSwitchAccount():

    email = "automation.hub2@mailinator.com"
    password = "ZXasqw12"
    url_hub = "https://test-z5y5zwrh0g.hub3c.com/"
    url_heo = "https://test-yyh773eb2l.hub3c.com/"
    company_name1 = "Auto Andrea"
    company_name2 = "Automation-HEO1"
    company_name3 = "Automation-HEO2"
    company_name4 = "Automation-Hub2"
    seq_company1 = 1
    seq_company2 = 2

    #1  Login as user with multiple business (same plan)
    def test_switch_same_plan(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email_address(self.email)
        login.input_password(self.password)
        login.click_login()
        login.select_company(self.seq_company1) #login as Auto Andrea
        login.click_ok()
        login.is_login_success()
        login.is_url_correct(self.url_hub)
        login.is_company_name_correct(self.company_name1)

    #2  Login as user with multiple business (different plan)
    def test_switch_different_plan(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/SignOut")
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email_address(self.email)
        login.input_password(self.password)
        login.click_login()
        login.select_company(self.seq_company2) #login as Automation-HEO1
        login.click_ok()
        login.is_login_success()
        login.is_url_correct(self.url_heo)
        login.is_company_name_correct(self.company_name2)

    #3  After login, switch user account to another business (on same plan)
    def test_switch_same_plan_from_profile(self):
        login.select_company_from_profile1()
        login.is_url_correct(self.url_heo)
        login.is_company_name_correct(self.company_name3)

    #4  After login, switch user account to another business (on different plan)
    def test_switch_different_plan_from_profile(self):
        login.select_company_from_profile2()
        login.is_url_correct(self.url_hub)
        login.is_company_name_correct(self.company_name4)
