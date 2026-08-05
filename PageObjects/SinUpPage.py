from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Utilities.wait import Wait


class SinUpPage:

# "//a[@data-bs-toggle='modal']"
    tagSignUp_xpath = "//span[@class='text-center']/a"
    dropdownRequestedFor_xpath = "//select[@id='type']"
    txtDOB_xpath = "//input[@id='dateofbirth']"
    txtFirstName_xpath = "//input[@id='firstname']"
    txtLastName_xpath = "//input[@id='lastname']"
    txtMobile_xpath = "//input[@id='mobile']"
    txtEmail_xpath = "//input[@id='emailid']"
    textareaAddress_xpath = "//textarea[@id='address']"
    btnSubmit_xpath = "//button[@id='enquirySubmitBtn']"

    def __init__(self, driver):
        self.driver = driver

    def clickonSignUp(self):
        Wait.wait_for_click(self.driver,(By.XPATH, self.tagSignUp_xpath)).click()

    def setEnqueryForm(self):
        request = Select(self.driver.find_element(By.XPATH, self.dropdownRequestedFor_xpath))
        request.select_by_visible_text("Retailer")
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys("01-02-1095")
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys("Shiv")
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys("Singh")
        self.driver.find_element(By.XPATH, self.txtMobile_xpath).send_keys("8888888889")
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys("shiv@gmail.com")
        self.driver.find_element(By.XPATH, self.textareaAddress_xpath).send_keys("Delhi")
        self.driver.find_element(By.XPATH, self.btnSubmit_xpath).click()