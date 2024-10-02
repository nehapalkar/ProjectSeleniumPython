import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_forgotten_passward:

    def test_forgotten_passward(self,setup_teardown):
        print("this is new account code execution")
        self.driver.find_element(By.LINK_TEXT,"forgotten passward?").click()
        time.sleep(3)