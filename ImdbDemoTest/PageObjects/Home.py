import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Home:
    def __init__(self,driver):
        self.driver=driver

    def movieRating(self,movieName):
        self.driver.find_element(By.XPATH,"//input[@type='text']").send_keys(movieName)
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//ul[@role='listbox']/li[1]"))).click()
        rating = self.driver.find_elements(By.XPATH,"//span[@class='sc-d541859f-1 imUuxf']")
        return rating[0].text

    def allMovieRating(self, list):
        ratings=[]
        for movie in list:
            self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(movie)
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']/li[1]"))).click()
            r = self.driver.find_elements(By.XPATH,"//span[@class='sc-d541859f-1 imUuxf']")
            ratings.append(r[0].text)
        return ratings

    def featuredTodayMethod(self):
        locator="//div[@class='ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--nowrap ipc-shoveler__grid']/div[@class='ipc-slate-card ipc-slate-card--baseAlt ipc-slate-card--media-radius ipc-slate-card--dynamic-width sc-20f6657c-0 khPucC imdb-editorial-single ipc-sub-grid-item ipc-sub-grid-item--span-4']/div/div/a/div"
        elementsList = self.driver.find_elements(By.XPATH,locator)
        fTList=[]
        for item in elementsList:
            fTList.append(item.text)
        return fTList

    def whatToWatch(self):
        locator="//a[@class='ipc-poster-card__title ipc-poster-card__title--clamp-2 ipc-poster-card__title--clickable']/span[@data-testid='title']"
        self.driver.find_element(By.XPATH,"//span[text()='Menu']").click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='What to Watch']"))).click()
        self.driver.find_element(By.XPATH,"//span[text()='MOST POPULAR']").click()
        #webElementslist = self.driver.find_elements(By.XPATH,locator)
        webElementlist = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,locator)))
        list=[]
        for i in webElementlist:
            list.append(i.text)
        return list


