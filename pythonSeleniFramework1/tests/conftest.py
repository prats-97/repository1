import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Below function is copied from Online, it is for setting up different browser at runtime via cmd terminal
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")      # assigning whatever value of browser we got from 'cmd terminal' to a local variable (browser_name) and using this local var now to check different browser conditions. Note: Value inside () of 'request.config.getoptions' should exactly match what it's defined in the above addoption function
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver=webdriver.Edge()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver=driver           # This statement means that: it sends the local 'driver' under setup() and assigns it to the class variable, called as 'driver' of TestOne() and now wherever, in class TestOne(), 'self.driver' keyword is used means its referring to the class variable means the driver in this case
    yield
    driver.close()



