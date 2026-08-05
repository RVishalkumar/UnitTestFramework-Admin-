from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class WalletPassbookPage:

    dropdownRole_xpath = "//select[@id='roleid']"
    dropdownRetailerName_xpath = "//select[@id='parentid']"
    dropdownStatus_xpath = "//select[@id='status']"
    txtDateRange_xpath = "//input[@id='reportrange']"
    btnSearch_xpath = "//button[@id='walletSubmit']"
    lnkVerificationPanel_xpath = "//*[@id='sidebar-menu']/li[13]"


    def __init__(self,driver):
        self.driver = driver

    def searchRetailerWalletPassbook(self):
        role=Select(self.driver.find_element(By.XPATH,self.dropdownRole_xpath))
        role.select_by_visible_text("Retailer")
        retailer=Select(self.driver.find_element(By.XPATH,self.dropdownRetailerName_xpath))
        retailer.select_by_visible_text("Vishal test (DEMORT00017)")
        status=Select(self.driver.find_element(By.XPATH,self.dropdownStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH,self.txtDateRange_xpath).send_keys("05-07-2026 - 05-08-2026")
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()
        if "passbook" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_13_WalletPassbookPage_WalletSuccessHistoryp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_13_WalletPassbookPage_WalletSuccessHistoryp.png")

    def clickonVerificationPanelMenu(self):
        self.driver.find_element(By.XPATH,self.lnkVerificationPanel_xpath).click()

