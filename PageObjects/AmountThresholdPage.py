from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AmountThresholdPage:

    dropdownRole_xpath = "//select[@id='roleid']"
    dropdownRetailer_xpath = "//select[@id='parentid']"
    btnSearch_xpath = "//button[@id='thresholdSubmit']"
    txtAmount_xpath = "//input[@id='amtlean']"
    btnSubmit_xpath = "//div[@id='content']/div/div/form/div[2]/button"
    lnkMerchantEnquiry_xpath = "//*[@id='sidebar-menu']/li[16]"


    def __init__(self,driver):
        self.driver = driver

    def setAmountThreshold(self):
        role=Select(self.driver.find_element(By.XPATH,self.dropdownRole_xpath))
        role.select_by_visible_text("Retailer")
        retailer=Select(self.driver.find_element(By.XPATH,self.dropdownRetailer_xpath))
        retailer.select_by_visible_text("DEMO RET TWO (DEMORT00002)")
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.txtAmount_xpath).send_keys("1000")
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()

    def clickonMerchantEnquiryMenu(self):
        self.driver.find_element(By.XPATH,self.lnkMerchantEnquiry_xpath).click()


