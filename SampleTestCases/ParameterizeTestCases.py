import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("username,passward",[("Neha","123"),("Akshay","12345"),("Swapnil","123456")])
def test_sample1(username,passward):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID,"email").send_keys(username)
    driver.find_element(By.ID,"pass").send_keys(passward)
    time.sleep(5)
