from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:

    def __init__(self,driver):
        self.driver=driver

    def countryLocation(self,countryVar):
        countryTextBox = (By.ID, "country")
        self.driver.find_element(*countryTextBox).send_keys(countryVar)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']"))).click()

    def termsCheckBox(self):
        termChBox = (By.XPATH, "//label[@for='checkbox2']")
        self.driver.find_element(*termChBox).click()

    def purchaseButton(self):
        btn = (By.XPATH, "//input[@type='submit']")
        self.driver.find_element(*btn).click()

    def confirmationMsg(self):
        confirmTextLocator = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        return self.driver.find_element(*confirmTextLocator).text
