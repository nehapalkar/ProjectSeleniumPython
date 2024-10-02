import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_Login_Page:

    @pytest.mark.parametrize("username,password",[("Neha","123"),("Deepi","1234"),("Swapnil","12345")])
    def test_login(self,setup_and_teardown,username,password):
        print("This is code for login")
        self.driver.find_element(By.ID,"email").send_keys(username)
        self.driver.find_element(By.ID,"pass").send_keys(password)
        time.sleep(1)

    def test_create_new_account(self,setup_and_teardown):
        print("This is code for Create new account")
        self.driver.find_element(By.LINK_TEXT, "Create new account").click()
        time.sleep(1)
