import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage


class HomePage():

    def __init__(self,driver):          # Constructor to bring the driver from test_Shope2e and use it here
        self.driver = driver


    def elements(self):
        shopLink = (By.XPATH, "//a[text()='Shop']")
        self.driver.find_element(*shopLink).click()             # Note: Mandatorily pass '*" before the shopLink for python to understand that shopLink is a Tuple data type only and nothing else
        checkOutPageObj = CheckOutPage(self.driver)
        return checkOutPageObj

    # For second test: test_FormPage.py

    def nameTextBox(self, NAME):
        nameBoxLoc = (By.XPATH,"//input[@name='name']")
        self.driver.find_element(*nameBoxLoc).send_keys(NAME)


    def emailTextBox(self,EMAIL):
        emailBoxLoc=(By.XPATH, "//input[@name='email']")
        self.driver.find_element(*emailBoxLoc).send_keys(EMAIL)

    def passwordBox(self,PASSWORD):
        passwordBoxLoc=(By.XPATH,"//input[@type='password']")
        self.driver.find_element(*passwordBoxLoc).send_keys(PASSWORD)

    def submitForm(self):
        submitBtnLoc=(By.XPATH, "//input[@value='Submit']")
        self.driver.find_element(*submitBtnLoc).click()
        time.sleep(3)
        self.driver.refresh()