from Utilities.BaseClass import BaseClass
from PageObjects.Home import Home
import openpyxl

class Test_two(BaseClass):
    def test_getFeaturedToday(self):
        homeObj = Home(self.driver)
        loggerObj = self.logsMethod()
        fTList = homeObj.featuredTodayMethod()
        excel = openpyxl.load_workbook("C:\\Users\\pratiyuk\\Pictures\\MovieList.xlsx")
        sheet = excel.active
        for i in range(0, len(fTList)):
            sheet.cell(row=i+2, column=7).value=fTList[i]
            loggerObj.info(fTList[i])
        excel.save("C:\\Users\\pratiyuk\\Pictures\\MovieList.xlsx")


