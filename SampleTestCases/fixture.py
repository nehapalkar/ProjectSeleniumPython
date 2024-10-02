# this program is for repeating code which is written before actual code, we write this is in "setup()"
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest, time
#
# @pytest.fixture()
# def setup():
#     global driver #global driver is for globally avaiable driver
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.facebook.com/")
#
# @pytest.mark.parametrize("username,password",[("Neha","123"),("Deepi","1234"),("Swapnil","12345")])
# def test_login(setup,username,password):
#     driver.find_element(By.ID,"email").send_keys(username)
#     driver.find_element(By.ID,"pass").send_keys(password)
#     time.sleep(5)
#     driver.close()
#
# def test_create_new_account(setup):
#     driver.find_element(By.LINK_TEXT,"Create new account").click()
#     time.sleep(5)
#     driver.close()

#-------------------------------------------------------------------------------------------------------------
#this code is for writing before and after repeated code which was written in code use set_and_teardown()
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture()
def setup_and_teardown():
    global driver
    print("This is common code before main code execution")
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    yield
    #code for log out
    driver.close()
    print("This is common code after execution of main code")

@pytest.mark.parametrize("username,password",[("Neha","123"),("Deepi","1234"),("Swapnil","12345")])
def test_login(setup_and_teardown,username,password):
    print("This is code for login")
    driver.find_element(By.ID,"email").send_keys(username)
    driver.find_element(By.ID,"pass").send_keys(password)
    time.sleep(3)


def test_create_new_account(setup_and_teardown):
    print("This is code for Create new account")
    driver.find_element(By.LINK_TEXT,"Create new account").click()
    time.sleep(3)
