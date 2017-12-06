from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest
import time

from connection import Connection
driver = Connection.driver

class Login(object):

    field_email_address_id = "Email"
    field_password_id = "Password"
    button_login = "//button[contains(text(),'Log in')]"
    link_registration = "/html/body/div[1]/div/div[1]/div/a[1]"
    link_forgot_password = "/html/body/div[1]/div/div[1]/div/a[2]"
    dropdown_select_company = "/html/body/div[1]/div/div/div/div[1]/span"
    button_ok_id = "btnSubmit"
    dropdown_switch_company_id = "btn-account-selector"
    dropdown_company_list1 = "/html/body/aside[3]/figure/div[3]/nav/ul/li[3]/a"
    dropdown_company_list2 = "/html/body/aside[3]/figure/div[3]/nav/ul/li[4]/a"

    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_id(self.field_email_address_id)
            self.driver.find_element_by_id(self.field_password_id)
            self.driver.find_element_by_xpath(self.button_login)
            self.driver.find_element_by_xpath(self.link_registration)
            self.driver.find_element_by_xpath(self.link_forgot_password)
            self.driver.find_element_by_xpath(self.dropdown_select_company)
            self.driver.find_element_by_id(self.button_ok_id)
            self.driver.find_element_by_id(self.dropdown_switch_company_id)
            self.driver.find_element_by_xpath(self.dropdown_company_list1)
            self.driver.find_element_by_xpath(self.dropdown_company_list2)
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

    def select_company(self, seq):
        scompany_el = self.driver.find_element_by_xpath(self.dropdown_select_company)
        scompany_el.click()
        time.sleep(2)

        for x in range(seq):
            scompany_el.send_keys(Keys.ARROW_DOWN)

        scompany_el.send_keys(Keys.ENTER)
        print("select company")

    def select_company_from_profile1(self):
        scompany_el = self.driver.find_element_by_id(self.dropdown_switch_company_id)
        scompany_el.click()
        time.sleep(3)
        comp_list = self.driver.find_element_by_xpath(self.dropdown_company_list1)
        comp_list.click()
        print("select company")

    def select_company_from_profile2(self):
        scompany_el = self.driver.find_element_by_id(self.dropdown_switch_company_id)
        scompany_el.click()
        time.sleep(3)
        comp_list = self.driver.find_element_by_xpath(self.dropdown_company_list2)
        comp_list.click()
        print("select company")

    def click_ok(self):
        ok_el = self.driver.find_element_by_id(self.button_ok_id)
        self.driver.execute_script("arguments[0].click();", ok_el) #using script so can be adjustable when using PhantomJS

    def is_login_success(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, ".//*[@id='new-message-link']")))
            print("test_login success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\login_failed.png")
            pytest.fail("test_login Failed")

    def is_url_correct(self, url):
        if driver.current_url == url :
            print("Correct URL")
        else:
            pytest.fail("Wrong URL")

    def is_company_name_correct(self, company_name):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), $company_name)]")))
            print("Company name is correct")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\display_warning_invalid_credentials_failed.png")
            pytest.fail("Company name not found/false")

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
            print("Redirect to test_registration page success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\directed_to_registration_page_failed.png")
            pytest.fail("Redirect to test_registration page failed")

    def is_directed_to_forgot_password_page(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "Email")))
            print("Redirect to forgot password page success")
        except TimeoutException:
            self.driver.get_screenshot_as_file("D:\\works\\hub3c_selenium\\log_test\\is_directed_to_forgot_password_page_failed.png")
            pytest.fail("Redirect to forgot password page failed")



