from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ManageLeadsPage:

    lnkAmountThreshold_xpath = "//*[@id='sidebar-menu']/li[15]"

    def __init__(self,driver):
        self.driver = driver

    def clickonAmountThreshold(self):
        self.driver.find_element(By.XPATH,self.lnkAmountThreshold_xpath).click()





