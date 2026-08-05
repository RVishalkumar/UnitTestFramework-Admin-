from selenium import webdriver
from selenium.webdriver.common.by import By


class VerificationPanelPage:

    lnkManageLeadsMenu_xpath = "//*[@id='sidebar-menu']/li[14]"

    def __init__(self,driver):
        self.driver = driver

    def clickonManageLeadsMenu(self):
        self.driver.find_element(By.XPATH,self.lnkManageLeadsMenu_xpath).click()