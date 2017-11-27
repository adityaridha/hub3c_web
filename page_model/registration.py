from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest

class Registration(object):

    field_company_name_id = "BusinessName"
    field_first_name_id = "FirstName"
    field_last_name_id = "LastName"
    field_email_address_id = "EmailAddress"
    field_password_id = "Password"
    field_repeat_password_id = "RepeatPassword"
    button_tnc = "html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div[7]/label/span"
    button_create_id = "button-submit"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_id(self.field_company_name_id)
            self.driver.find_element_by_id(self.field_first_name_id)
            self.driver.find_element_by_id(self.field_last_name_id)
            self.driver.find_element_by_id(self.field_email_address_id)
            self.driver.find_element_by_id(self.field_password_idpassword_id)
            self.driver.find_element_by_id(self.field_repeat_password_id)
            self.driver.find_element_by_xpath(self.button_tnc)
            self.driver.find_element_by_id(self.button_create_id)
            print("\nall element ready")
        except NoSuchElementException:
            pytest.fail("Some element not ready")

    def input_company_name(self, company_name):
        company_el = self.driver.find_element_by_id(self.field_company_name_id)
        company_el.clear()
        company_el.send_keys(company_name)
        print("input company name")

    def input_first_name(self, first_name):
        fname_el = self.driver.find_element_by_id(self.field_first_name_id)
        fname_el.clear()
        fname_el.send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        lname_el = self.driver.find_element_by_id(self.field_last_name_id)
        lname_el.clear()
        lname_el.send_keys(last_name)
        print("input last name")

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

    def input_repeat_password(self, password):
        rpass_el = self.driver.find_element_by_id(self.field_repeat_password_id)
        rpass_el.clear()
        rpass_el.send_keys(password)
        print("input repeat password")

    def tick_tnc(self):
        tnc_el = self.driver.find_element_by_id(self.button_tnc)
        tnc_el.click()
        print("tick tnc")

    def create_account(self):
        create_el = self.driver.find_element_by_xpath(self.button_create_id)
        create_el.click()
        print("click create")

    def is_registration_success(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "html/body/div[1]/div/div[1]/form/div[5]/div/button")))
            print("Registration success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\registration_failed.png")
            pytest.fail("Registration Failed")