from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest

class Login(object):

    username_id = "Email"
    password_id = "Password"
    sign_in_button = "//button[contains(text(),'Log in')]"
    registration_button = "/html/body/div[1]/div/div[1]/div/a[1]"
    forgot_password_button = "/html/body/div[1]/div/div[1]/div/a[2]"


    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            self.driver.find_element_by_id(self.username_id)
            self.driver.find_element_by_id(self.password_id)
            self.driver.find_element_by_xpath(self.sign_in_button)
            print("\nall element ready")
        except NoSuchElementException:
            pytest.fail("Some element not ready")

    def input_email(self, email):
        username_el = self.driver.find_element_by_id(self.username_id)
        username_el.clear()
        username_el.send_keys(email)
        print("input email")

    def input_password(self, password):
        pass_el = self.driver.find_element_by_id(self.password_id)
        pass_el.clear()
        pass_el.send_keys(password)
        print("input password")

    def sign_in(self):
        sign_in_el = self.driver.find_element_by_xpath(self.sign_in_button)
        self.driver.execute_script("arguments[0].click();", sign_in_el) #using script so can be adjustable when using PhantomJS

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



