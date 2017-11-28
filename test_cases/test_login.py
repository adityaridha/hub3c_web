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

class TestLogin():

    def test_login_logout(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email("marsha@freehub.com")
        login.input_password("ZXasqw12")
        login.sign_in()
        login.is_login_success()


