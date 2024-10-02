import pytest

@pytest.mark.regression
def test_demo_sample1():
    print("This is test case 1")

@pytest.mark.skip
def test_demo_sample2():
    print("This is test Case 2")