import time

import pytest

from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

class TestFormPage(BaseClass):                  # using that same BaseClass and same fixture (setup in conftest.py) as the link is same for this test too (just like Shope2e)
    def test_formPage(self,dataInputFix):

        homeObj = HomePage(self.driver)
        logObj = self.test_logsMethod()

        homeObj.nameTextBox(dataInputFix[0])
        logObj.info("Giving first name Input : "+dataInputFix[0])

        homeObj.emailTextBox(dataInputFix[1])
        logObj.info("Giving Email Input : "+dataInputFix[1])

        logObj.info("Giving Password as Input : "+dataInputFix[2])
        homeObj.passwordBox(dataInputFix[2])

        logObj.info("Clicking submit button")
        homeObj.submitForm()

    @pytest.fixture(params=[("Rahul","rah@gmail.com","Hello"),("Suraj","suraj@gmail.com","Hello1")])
    def dataInputFix(self,request):
        return request.param

    # If you have to use dictionary in the fixture method under params then you can use below, just replace with below in line 26
    # params=[{"Name":"Rahul", "Email":"rah@gmail.com"}, {"Name":"Suraj", "Email":"suraj@gmail.com"}]
    # Also, if using dictionary, then in line 15 and 18 use like : dataInputFix["Name"] and dataInputFix["Email"]