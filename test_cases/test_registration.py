import sys
import os
import pytest
import time
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)

from page_model import Login
from page_model import Registration
from connection import Connection

driver = Connection.driver
login = Login(driver)
regis = Registration(driver)

class TestRegistration():

    def test_registration(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/Index")
        regis.input_company_name("Automation-Hub")
        regis.input_first_name("Auto")
        regis.input_last_name("Hub")
        regis.input_email_address("automation.hub1@mailinator.com")
        regis.input_password("ZXasqw12")
        regis.input_repeat_password("ZXasqw12")
        regis.tick_tnc()
        regis.create_account()
        regis.is_registration_success()
