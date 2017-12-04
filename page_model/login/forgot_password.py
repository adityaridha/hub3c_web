from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest

class Forgot(object):

    field_email_address_id = "Email"
    button_reset = "/html/body/div/div[2]/div/form/div[2]/input"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_id(self.field_email_address_id)
            self.driver.find_element_by_xpath(self.button_reset)
            print("\nall element ready")
        except NoSuchElementException:
            pytest.fail("Some element not ready")

    def input_email_address(self, email):
        email_el = self.driver.find_element_by_id(self.field_email_address_id)
        email_el.clear()
        email_el.send_keys(email)
        print("input email")

    def click_reset(self):
        reset_el = self.driver.find_element_by_xpath(self.button_reset)
        self.driver.execute_script("arguments[0].click();", reset_el) #using script so can be adjustable when using PhantomJS

    def is_reset_success(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'An email has successfully sent. Please check your inbox and follow the instructions.')]")))
            print("test_reset success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\login_failed.png")
            pytest.fail("test_reset Failed")

    def is_reset_fail(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'The Email you entered does not exist. Please try again.')]")))
            print("Unregistered email ")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_invalid_credentials_failed.png")
            pytest.fail("Warning was not displayed")

    def is_email_address_invalid(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Email address is invalid.')]")))
            print("Email is invalid")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_email_address_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_email_address_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Required.')]")))
            print("Email name is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_email_address_empty_failed.png")
            pytest.fail("Warning was not displayed")
