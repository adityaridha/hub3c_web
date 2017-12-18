import sys
import os
import pytest
import time
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)

from page_model import Login
from connection import Connection

driver = Connection.driver
login = Login(driver)

@pytest.mark.usefixtures("reset_url")
class TestLogin():


    def test_login_logout(self):
        login.input_email_address("marsha@freehub.com")
        login.input_password("ZXasqw12")
        login.click_login()
        login.is_login_success()

    def test_wrong_login(self):
        login.input_email_address("marsha@freehub.com")
        login.input_password("ZXasqw12")
        login.click_login()
        login.is_login_success()





