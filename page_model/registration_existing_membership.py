from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest
import time

class Registration_Existing_Membership (object):

    field_email_address_id = "ExistingUserName"
    field_password_id = "ExistingPassword"
    button_login_id = "button-login"
    dropdown_salutation = "html/body/div[1]/div[3]/div/div[2]/div[1]/form/div[2]/span/span"
    dropdown_select_salutation = "//*[contains(text(), 'Please select salutation')]"
    #field_first_name_id = "FirstName"
    #field_last_name_id = "LastName"
    #button_tnc = "html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div[7]/label"
    #button_create_id = "button-submit"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_id(self.field_email_address_id)
            self.driver.find_element_by_id(self.field_password_id)
            self.driver.find_element_by_id(self.button_login_id)
            self.driver.find_element_by_xpath(self.dropdown_salutation)
            self.driver.find_element_by_xpath(self.dropdown_salutation_select_salutation)
            print("\nall element ready")
        except NoSuchElementException:
            pytest.fail("Some element not ready")

    def input_email_address(self, email_address):
        email_el = self.driver.find_element_by_id(self.field_email_address_id)
        email_el.clear()
        email_el.send_keys(email_address)
        print("input email address")

    def input_password(self, password):
        pass_el = self.driver.find_element_by_id(self.field_password_id)
        pass_el.clear()
        pass_el.send_keys(password)
        print("input password")

    def click_login(self):
        login_el = self.driver.find_element_by_id(self.button_login_id)
        login_el.click()
        print("click login")

    def select_salutation(self):
        salutation_el = self.driver.find_element_by_xpath(self.dropdown_salutation)
        salutation_el.click()
        salutation_el.send_keys(Keys.DOWN + Keys.ENTER)
        #time.sleep(1)
        #mr_el = self.driver.find_element_by_xpath(self.dropdown_salutation_select_salutation)
        #mr_el.click()
        print("select salutation")

    def is_directed_to_registration_page(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "BusinessName")))
            print("Login success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\registration_failed.png")
            pytest.fail("Login Failed")

    def is_login_fail(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'User Name or Password invalid')]")))
            print("User Name or Password is invalid ")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\registration_failed.png")
            pytest.fail("Warning was not displayed")
