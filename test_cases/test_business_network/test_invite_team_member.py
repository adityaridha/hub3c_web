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
from faker import Factory

driver = Connection.driver
network = page_model.Networks(driver)
team_member = page_model.TeamMember(driver)
login = page_model.Login(driver)

class TestInviteTeamMember():

    fake = Factory.create()
    name = fake.first_name() + fake.last_name()
    email_invite = name + "@mailinator.com"
    email = "auto1@mailinator.com"
    password = "ZXasqw12"

    #1 test send invitation to team member
    def test_invite_team_member(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/")
        login.input_email_address(self.email)
        login.input_password(self.password)
        login.click_login()

        time.sleep(2)
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Home/Networks")

        network.verify_all_element()
        network.click_invite()
        time.sleep(1)
        network.click_invite_team_member()
        time.sleep(2)

        team_member.verify_all_element()
        team_member.input_name(self.name)
        team_member.input_email(self.email_invite)
        team_member.click_send()
        team_member.is_invite_success()