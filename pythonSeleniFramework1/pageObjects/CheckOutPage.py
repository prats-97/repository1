from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver=driver

    def productsList(self):
        productsListLocator = (By.XPATH, "//div[@class='card h-100']")
        return self.driver.find_elements(*productsListLocator)

    def checkOutButton(self):
        chkoutbutton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
        self.driver.find_element(*chkoutbutton).click()

    def successButton(self):
        successChkBtn = (By.XPATH, "//button[@class='btn btn-success']")
        self.driver.find_element(*successChkBtn).click()
        confirmPageObj = ConfirmPage(self.driver)
        return confirmPageObj