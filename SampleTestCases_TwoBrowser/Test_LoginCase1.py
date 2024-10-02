import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class Test_Login_Page:

    def test_login(self,setup_teardown):
        print("This is login code")
        self.driver.find_element(By.ID,"email").send_keys("Neha")
        self.driver.find_element(By.ID,"pass").send_keys("1234")
        time.sleep(3)

    def test_create_new_account(self,setup_teardown):
        print("This is create new account code")
        self.driver.find_element(By.ID,"Create new account").click()
        time.sleep(3)
