import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage

class TestOne(BaseClass):

    def test_shopPhone(self):
        self.driver.implicitly_wait(4)

        #1.  Home page
        homeOBJ = HomePage(self.driver)
        checkOutPageObj = homeOBJ.elements()                          # Old : self.driver.find_element(By.XPATH, "//a[text()='Shop']").click(). Also, no need to create the object for the CheckOutPage explicitly in this main test. It's already created in Home class only (and returned) after the last element is clicked in Home page after which new page is Check Out page only

        #2. Checkout page
        products = checkOutPageObj.productsList()                                       # Old : self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        time.sleep(3)

        # traversing through each product, using Chaining of elements to find (like webElement.find_element)
        for product in products:
            proName = product.find_element(By.XPATH, "div/h4/a").text
            if proName == 'Blackberry':
                product.find_element(By.XPATH, "div/button").click()

        # One important thing to remember, WHENEVER WORKING ON CHAINING OF WEB ELEMENTS, THEN WITHIN (2ND) XPATH WILL ALWAYS START WITHOUT '/' ELSE YOU WILL GET DIFFERENT OUTPUT.
        # and properly check in DOM of the web page if you are able to find the correct hierarchy of parent to child element for this chaining

        checkOutPageObj.checkOutButton()                                           #Old : self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        confirmPageObj = checkOutPageObj.successButton()                           #Old : self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        # 3. Confirm page
        confirmPageObj.countryLocation("Ame")                                      #Old : self.driver.find_element(By.ID, "country").send_keys("Ame")
        confirmPageObj.termsCheckBox()                                              #Old : self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        confirmPageObj.purchaseButton()                                             #Old : self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        assert "Success" in confirmPageObj.confirmationMsg()                        #Old : self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        time.sleep(2)