import pytest

@pytest.mark.smoke
def test_demo_testcase1():
    print("This is test case 1")

@pytest.mark.smoke
def test_demo_testcase2():
    print("This is test case 1")

@pytest.mark.regression
def test_demo_testcase3():
    print("This is test case 1")