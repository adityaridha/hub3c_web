from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest

class Networks(object):

    button_invite = '//*[@id="app-content"]/div/nav/a[1]'
    button_invite_team_member_id = "btn-invite-teammember"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_xpath(self.button_invite)
            # self.driver.find_element_by_id(self.button_invite_team_member_id)
            print("\nall element ready")
        except NoSuchElementException:
            pytest.fail("Some element not ready")

    def click_invite(self):
        invite_el = self.driver.find_element_by_xpath(self.button_invite)
        self.driver.execute_script("arguments[0].click();", invite_el) #using script so can be adjustable when using PhantomJS
        print("click invite")

    def click_invite_team_member(self):
        invite_team_el = self.driver.find_element_by_id(self.button_invite_team_member_id)
        self.driver.execute_script("arguments[0].click();", invite_team_el) #using script so can be adjustable when using PhantomJS
        print("click invite team member")