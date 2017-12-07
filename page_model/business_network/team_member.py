from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest

class TeamMember(object):

    field_name_id = "textbox-name1"
    field_email_id = "textbox-email1"
    button_invite_id = "button-sendMultiple"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_id(self.field_name_id)
            self.driver.find_element_by_id(self.field_email_id)
            self.driver.find_element_by_id(self.button_invite_id)
            print("\nall element ready")
        except NoSuchElementException:
            pytest.fail("Some element not ready")

    def input_name(self, name):
        name_el = self.driver.find_element_by_id(self.field_name_id)
        name_el.send_keys(name)
        print("input name")

    def input_email(self, email):
        email_el = self.driver.find_element_by_id(self.field_email_id)
        email_el.send_keys(email)
        print("input email")

    def click_send(self):
        invite_el = self.driver.find_element_by_id(self.button_invite_id)
        invite_el.click()

    def is_invite_success(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'You have successfully sent the invitation.')]")))
            print("test_invite success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\login_failed.png")
            pytest.fail("test_invite Failed")