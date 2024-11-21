from Utilities.BaseClass import BaseClass
from PageObjects.Home import Home


class Test_three(BaseClass):
    def test_whatToWatch(self):
        homeObj = Home(self.driver)
        list = homeObj.whatToWatch()
        print(len(list))
        for i in list:
            print(i)


