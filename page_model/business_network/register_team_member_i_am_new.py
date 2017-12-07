from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest
import time

class TeamMemberNew(object):
    dropdown_salutation = "/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div[2]/span"
    dropdown_salutation_mr = "//*[@id='Title_listbox']/li[2]"
    field_first_name_id = "FirstName"
    field_last_name_id = "LastName"
    field_email_address_id = "PreferredEmailAddress"
    field_repeat_email_address_id = "ConfirmPreferredEmailAddress"
    field_password_id = "Password"
    field_repeat_password_id = "RepeatPassword"
    button_tnc_xpath = "/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div[9]/label"
    button_save_id = "button-continue"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_xpath(self.dropdown_salutation)
            self.driver.find_element_by_xpath(self.dropdown_salutation_mr)
            self.driver.find_element_by_id(self.field_first_name_id)
            self.driver.find_element_by_id(self.field_last_name_id)
            self.driver.find_element_by_id(self.field_email_address_id)
            self.driver.find_element_by_id(self.field_repeat_email_address_id)
            self.driver.find_element_by_id(self.field_password_id)
            self.driver.find_element_by_id(self.field_repeat_password_id)
            self.driver.find_element_by_xpath(self.button_tnc_xpath)
            self.driver.find_element_by_id(self.button_save_id)
            print("\nall element ready")
        except NoSuchElementException:
            pytest.fail("Some element not ready")

    def select_salutation(self):
        salutation_el = self.driver.find_element_by_xpath(self.dropdown_salutation)
        salutation_el.click()
        time.sleep(1)
        mr_el = self.driver.find_element_by_xpath(self.dropdown_salutation_mr)
        mr_el.click()
        print("select salutation")

    def input_first_name(self, first_name):
        first_name_el = self.driver.find_element_by_id(self.field_first_name_id)
        first_name_el.send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        last_name_el = self.driver.find_element_by_id(self.field_last_name_id)
        last_name_el.send_keys(last_name)
        print("input last name")

    def input_email(self, email):
        email_el = self.driver.find_element_by_id(self.field_email_address_id)
        email_el.send_keys(email)
        print("input email")

    def input_repeat_email(self, repeat_email):
        repeat_email_el = self.driver.find_element_by_id(self.field_repeat_email_address_id)
        repeat_email_el.send_keys(repeat_email)
        print("input repeat email")

    def input_password(self, password):
        password_el = self.driver.find_element_by_id(self.field_password_id)
        password_el.send_keys(password)
        print("input password")

    def input_repeat_password(self, repeat_password):
        password_email_el = self.driver.find_element_by_id(self.field_repeat_password_id)
        password_email_el.send_keys(repeat_password)
        print("input repeat password")

    def tick_tnc(self):
        tnc_el = self.driver.find_element_by_xpath(self.button_tnc_xpath)
        tnc_el.click()
        print("tick tnc")

    def click_save(self):
        save_el = self.driver.find_element_by_id(self.button_save_id)
        save_el.click()
        print("click save")

    def is_register_success(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'You have successfully created your new account. Now please login using the credentials you just created.')]")))
            print("test_register success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\register_failed.png")
            pytest.fail("test_register Failed")

    def is_email_already_exist(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Email Address you entered already exists.')]")))
            print("Email address already exist")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\register_failed.png")
            pytest.fail("Warning was not displayed")

    def is_first_name_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'First Name is required')]")))
            print("First name is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_first_name_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_last_name_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Last Name is required')]")))
            print("Last name is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_last_name_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_email_address_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Email Address is required')]")))
            print("Email address is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_email_address_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_repeat_email_address_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Repeat Email Address is required')]")))
            print("Email address is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_repeat_email_address_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_email_unmatched(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Email address did not match.')]")))
            print("Password is unmatched")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_email_unmatched_failed.png")
            pytest.fail("Warning was not displayed")

    def is_password_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Password is required')]")))
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
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Password must contain at least 6-20 characters, 1 number, 1 upper case character and 1 lower case character.')]")))
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