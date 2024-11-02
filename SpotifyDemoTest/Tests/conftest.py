import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser=request.config.getoption("--browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome()
    if browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.get("https://open.spotify.com/")
    time.sleep(3)
    request.cls.driver = driver
    yield
    driver.close()


