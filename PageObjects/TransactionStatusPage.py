from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TransactionStatusPage:

    dropdownServiceList_xpath = "//select[@id='service']"


    def __init__(self,driver):
        self.driver = driver

    def checkTransactionStatus(self):
        list=Select(self.driver.find_element(By.XPATH,self.dropdownServiceList_xpath))