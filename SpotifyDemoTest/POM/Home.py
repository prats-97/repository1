import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Home:
    def __init__(self, driver):
        self.driver = driver

    def getAlbumsList(self):
        locator = "//section[@aria-label='Popular albums']/div[@data-testid='grid-container']/div[@data-encore-id='card']//div[@class='Areas__InteractiveArea-sc-1tea2mc-0 Areas__Column-sc-1tea2mc-2 MWEhk yMCdi']/a[@class='Gi6Lr1whYBA2jutvHvjQ']/p[@data-encore-id='cardTitle']/span[@class='CardTitle__LineClamp-sc-1h38un4-0 RBShQ']"
        list = self.driver.find_elements(By.XPATH, locator)
        return list

    def getSeeAllList(self):
        seeAllLocator= "//section[@aria-label='Popular albums']/div[@class='q8AZzDc_1BumBHZg0tZb']/div[@role='group']/div[@class='Areas__HeaderArea-sc-8gfrea-3 TJKQw']/div[@class='Areas__InteractiveArea-sc-8gfrea-0 Areas__TrailingSlot-sc-8gfrea-7 bJSfgC jpzxju']/a[@href='/section/0JQ5DAnM3wGh0gz1MXnu3B']"
        locator1 = "//section[@aria-label='Popular albums']/div[@data-testid='grid-container']/div[@data-encore-id='card']//div[@class='Areas__InteractiveArea-sc-1tea2mc-0 Areas__Column-sc-1tea2mc-2 MWEhk yMCdi']/a[@class='Gi6Lr1whYBA2jutvHvjQ']/p[@data-encore-id='cardTitle']/span[@class='CardTitle__LineClamp-sc-1h38un4-0 RBShQ']"

        wait = WebDriverWait(self.driver, 10)

        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, seeAllLocator))).click()
        seeAlllist = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, locator1)))
        return seeAlllist
