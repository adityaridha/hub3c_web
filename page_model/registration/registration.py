from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest
import time

class Registration(object):

    field_company_name_id = "BusinessName"
    dropdown_salutation = "/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div[2]/span"
    dropdown_salutation_mr = "//*[@id='Title_listbox']/li[2]"
    field_first_name_id = "FirstName"
    field_last_name_id = "LastName"
    field_email_address_id = "EmailAddress"
    field_password_id = "Password"
    field_repeat_password_id = "RepeatPassword"
    button_tnc = "/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div[7]/label"
    button_create_id = "button-submit"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_id(self.field_company_name_id)
            self.driver.find_element_by_xpath(self.dropdown_salutation)
            self.driver.find_element_by_xpath(self.dropdown_salutation_mr)
            self.driver.find_element_by_id(self.field_first_name_id)
            self.driver.find_element_by_id(self.field_last_name_id)
            self.driver.find_element_by_id(self.field_email_address_id)
            self.driver.find_element_by_id(self.field_password_id)
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

    def select_salutation(self):
        salutation_el = self.driver.find_element_by_xpath(self.dropdown_salutation)
        salutation_el.click()
        time.sleep(1)
        mr_el = self.driver.find_element_by_xpath(self.dropdown_salutation_mr)
        mr_el.click()
        print("select salutation")

    def input_first_name(self, first_name):
        fname_el = self.driver.find_element_by_id(self.field_first_name_id)
        fname_el.clear()
        fname_el.send_keys(first_name)
        print("input first name")

    def clear_first_name(self):
        clear_fname_el = self.driver.find_element_by_id(self.field_first_name_id)
        clear_fname_el.clear()

    def input_last_name(self, last_name):
        lname_el = self.driver.find_element_by_id(self.field_last_name_id)
        lname_el.clear()
        lname_el.send_keys(last_name)
        print("input last name")

    def clear_last_name(self):
        clear_lname_el = self.driver.find_element_by_id(self.field_last_name_id)
        clear_lname_el.clear()

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
        tnc_el = self.driver.find_element_by_xpath(self.button_tnc)
        tnc_el.click()
        print("tick tnc")

    def create_account(self):
        create_el = self.driver.find_element_by_id(self.button_create_id)
        create_el.click()
        print("click create")

    def is_registration_success(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Log in')]")))
            print("test_registration success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\registration_failed.png")
            pytest.fail("test_registration Failed")

    def is_company_name_exist(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Company Name or Family Name already exists.')]")))
            print("Company name is already exist")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_company_name_exist_failed.png")
            pytest.fail("Warning was not displayed")

    def is_email_address_exist(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Email Address you entered already exists.')]")))
            print("Email address is already exist")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_email_address_exist_failed.png")
            pytest.fail("Warning was not displayed")

    def is_company_name_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Business name required')]")))
            print("Company name is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_company_name_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_first_name_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'First Name required')]")))
            print("First name is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_first_name_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_last_name_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Last Name required')]")))
            print("Last name is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_last_name_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_email_address_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Email required')]")))
            print("Email address is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_email_address_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_password_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Password required')]")))
            print("Password is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_password_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_repeat_password_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Repeat Password required')]")))
            print("Repeat password is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_repeat_password_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_password_unmatched(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Password did not match.')]")))
            print("Password is unmatched")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_password_unmatched_failed.png")
            pytest.fail("Warning was not displayed")

    def is_password_invalid(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Password must contain at least 6-20 characters')]")))
            print("Password is invalid")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_password_invalid_failed.png")
            pytest.fail("Warning was not displayed")

    def is_email_address_invalid(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Email address is invalid.')]")))
            print("Email address is invalid")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_email_address_invalid_failed.png")
            pytest.fail("Warning was not displayed")
