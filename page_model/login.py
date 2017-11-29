from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest

class Login(object):

    field_email_address_id = "Email"
    field_password_id = "Password"
    button_login = "//button[contains(text(),'Log in')]"
    link_registration = "/html/body/div[1]/div/div[1]/div/a[1]"
    link_forgot_password = "/html/body/div[1]/div/div[1]/div/a[2]"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_id(self.field_email_address_id)
            self.driver.find_element_by_id(self.field_password_id)
            self.driver.find_element_by_xpath(self.button_login)
            self.driver.find_element_by_xpath(self.link_registration)
            self.driver.find_element_by_xpath(self.link_forgot_password)
            print("\nall element ready")
        except NoSuchElementException:
            pytest.fail("Some element not ready")

    def input_email_address(self, email):
        email_el = self.driver.find_element_by_id(self.field_email_address_id)
        email_el.clear()
        email_el.send_keys(email)
        print("input email")

    def input_password(self, password):
        pass_el = self.driver.find_element_by_id(self.field_password_id)
        pass_el.clear()
        pass_el.send_keys(password)
        print("input password")

    def click_login(self):
        login_el = self.driver.find_element_by_xpath(self.button_login)
        self.driver.execute_script("arguments[0].click();", login_el) #using script so can be adjustable when using PhantomJS

    def go_to_registration(self):
        regis_el = self.driver.find_element_by_link_text("Register as a new user")
        regis_el.click()

    def go_to_forgot_password(self):
        forgot_el = self.driver.find_element_by_link_text("Forgot your password?")
        forgot_el.click()

    def is_login_success(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, ".//*[@id='new-message-link']")))
            print("Login success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\login_failed.png")
            pytest.fail("Login Failed")

    def is_login_fail(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid credentials')]")))
            print("User Name or Password is invalid ")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_invalid_credentials_failed.png")
            pytest.fail("Warning was not displayed")

    def is_email_address_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'The Email field is required.')]")))
            print("Company name is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_email_address_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_password_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'The Password field is required.')]")))
            print("Password is empty")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_password_empty_failed.png")
            pytest.fail("Warning was not displayed")

    def is_directed_to_registration_page(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "BusinessName")))
            print("Redirect to Registration page success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\directed_to_registration_page_failed.png")
            pytest.fail("Redirect to Registration page failed")

    def is_directed_to_forgot_password_page(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "Email")))
            print("Redirect to forgot password page success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\is_directed_to_forgot_password_page_failed.png")
            pytest.fail("Redirect to forgot password page failed")



