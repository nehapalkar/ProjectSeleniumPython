import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_Demo:

    def test_forgotten_account(self,setup_and_teardown):
        self.driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
        print("forgotten account testcase")
        time.sleep(3)