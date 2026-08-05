from selenium import webdriver
from selenium.webdriver.common.by import By

class ServicePanelPage:

    btnCMS_xpath = "//input[@id='switch-19']"
    btnPayout_xpath = "//input[@id='switch-3']"
    lnkWalletPassbook_xpath = "//*[@id='sidebar-menu']/li[12]"

    def __init__(self,driver):
        self.driver = driver

    def controlCMSServicePanel(self):
        self.driver.find_element(By.XPATH,self.btnCMS_xpath).click()
        if "servicepanel" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_12_ServicePanelPage_CMSServicePanelp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_12_ServicePanelPage_CMSServicePanelf.png")
        self.driver.find_element(By.XPATH,self.btnCMS_xpath).click()

    def controlPayoutServicePanel(self):
        self.driver.find_element(By.XPATH, self.btnPayout_xpath).click()
        if "servicepanel" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_12_ServicePanelPage_PayoutServicePanelp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_12_ServicePanelPage_PayoutServicePanelf.png")
        self.driver.find_element(By.XPATH, self.btnPayout_xpath).click()


    def clickonWalletPassbookMenu(self):
        self.driver.find_element(By.XPATH,self.lnkWalletPassbook_xpath).click()

