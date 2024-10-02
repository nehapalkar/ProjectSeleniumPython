import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome","edge"])
def setup_teardown(request):
    global driver
    print("This is common code before the main code")

    if request.param == "chrome":
       driver=webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    request.cls.driver = driver

    yield
    driver.close()
    print("this is common end code")