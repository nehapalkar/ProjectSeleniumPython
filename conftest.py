#here we have to write code which was repeated in program,remember to write this file outside the SampleTestCases file,
#otherwise it won't be able to work.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def setup_and_teardown(request):#here we are making request for driver
    global driver
    print("This is common code before the main code execution")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    request.cls.driver = driver#here we are requesting any class to access driver from here
    yield
    #code for log out
    driver.close()
    print("This is common code after execution of the main code")