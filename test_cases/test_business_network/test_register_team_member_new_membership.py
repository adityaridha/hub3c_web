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
register = page_model.TeamMemberNew(driver)
login = page_model.Login(driver)

class TestRegisterTeamMemberNewMembership():

    fake = Factory.create()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = first_name + last_name + "@mailinator.com"
    first_name1 = fake.first_name()
    last_name1 = fake.last_name()
    email1 = first_name + last_name + "@mailinator.com"
    first_name2 = fake.first_name()
    last_name2 = fake.last_name()
    email2 = first_name2 + last_name2 + "@mailinator.com"
    password = "ZXasqw12"

    #1 test register team member with new membership
    def test_register_team_member(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name1)
        register.input_last_name(self.last_name1)
        register.input_email(self.email1)
        register.input_repeat_email(self.email1)
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_register_success()
        login.input_email_address(self.email)
        login.input_password(self.password)
        login.click_login()
        time.sleep(1)

    #2 test register team member w/o salutation
    def test_register_team_member_no_salutation(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/SignOut")
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        register.input_first_name(self.first_name2)
        register.input_last_name(self.last_name2)
        register.input_email(self.email2)
        register.input_repeat_email(self.email2)
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_register_success()
        login.input_email_address(self.email)
        login.input_password(self.password)
        login.click_login()
        time.sleep(1)

    #3 test register team member using existing email
    def test_register_team_member_existing_email(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Account/SignOut")
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email("hub1@mailinator.com")
        register.input_repeat_email("hub1@mailinator.com")
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_email_already_exist()

    #4 test register team member by emptying all mandatory fields
    def test_register_team_member_empty(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        register.verify_all_element()
        register.tick_tnc()
        register.click_save()
        register.is_first_name_empty()
        register.is_last_name_empty()
        register.is_email_address_empty()
        register.is_repeat_email_address_empty()
        register.is_password_empty()

    #5 test register team member by emptying first name
    def test_register_team_member_empty_first_name(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_first_name_empty()

    #6 test register team member by emptying last name
    def test_register_team_member_empty_last_name(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_last_name_empty()

    #7 test register team member by emptying email
    def test_register_team_member_empty_email(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_repeat_email(self.email)
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_email_address_empty()

    #8 test register team member by emptying repeat email
    def test_register_team_member_empty_repeat_email(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_repeat_email_address_empty()

    #9 test register team member by emptying password
    def test_register_team_member_empty_password(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_password_empty()

    #10 test register team member by emptying repeat password
    def test_register_team_member_empty_repeat_password(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_password_unmatched()

    #11 test register team member unmatch password
    def test_register_team_member_unmatch_password(self):
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_password(self.password)
        register.input_repeat_password("zxasqw12")
        register.tick_tnc()
        register.click_save()
        register.is_password_unmatched()

    #12 test register team member invalid password
    def test_register_team_member_invalid_password(self):
        # without uppercase
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_password("zxasqw12")
        register.input_repeat_password("zxasqw12")
        register.tick_tnc()
        register.click_save()
        register.is_password_invalid()

        time.sleep(2)
        # without lowercase
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_password("ZXASQW12")
        register.input_repeat_password("ZXASQW12")
        register.tick_tnc()
        register.click_save()
        register.is_password_invalid()

        time.sleep(2)
        # without number
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_password("ZXasqw")
        register.input_repeat_password("ZXasqw")
        register.tick_tnc()
        register.click_save()
        register.is_password_invalid()

        time.sleep(2)
        # <6 chars
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email(self.email)
        register.input_repeat_email(self.email)
        register.input_password("Zaq1")
        register.input_repeat_password("Zaq1")
        register.tick_tnc()
        register.click_save()
        register.is_password_invalid()

    #13 test register team member incorrect email
    def test_register_team_member_incorrect_email(self):
        # without @
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email("auto1mailinator.com")
        register.input_repeat_email("auto1mailinator.com")
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_email_address_invalid()

        time.sleep(2)
        # without dot (.) after @
        driver.get("https://test-z5y5zwrh0g.hub3c.com/Join/JoinAdviser?BID=!bQ%2fcvEhYxxm!6XiIZvF!Q%3d%3d")
        # register.verify_all_element()
        register.select_salutation()
        register.input_first_name(self.first_name)
        register.input_last_name(self.last_name)
        register.input_email("auto1@mailinatorcom")
        register.input_repeat_email("auto1@mailinatorcom")
        register.input_password(self.password)
        register.input_repeat_password(self.password)
        register.tick_tnc()
        register.click_save()
        register.is_email_address_invalid()