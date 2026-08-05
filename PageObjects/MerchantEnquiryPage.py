from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys


class MerchantEnquiryPage:

    searchMerchantEnquiry_xpath = "//input[@id='usersearchInput']"
    lnkTransactionStatusMenu_xpath = "//*[@id='sidebar-menu']/li[17]"

    def __init__(self,driver):
        self.driver = driver

    def searchMerchantList(self):
        self.driver.find_element(By.XPATH,self.searchMerchantEnquiry_xpath).send_keys("9407271094")
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()
        if "enquiry" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_17_MerchantEnquiryPage_RetailerDetailsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_17_MerchantEnquiryPage_RetailerDetailsf.png")

    def clickonTransactionStatusMenu(self):
        self.driver.find_element(By.XPATH,self.lnkTransactionStatusMenu_xpath).click()
