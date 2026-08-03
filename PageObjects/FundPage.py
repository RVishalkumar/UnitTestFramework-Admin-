from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class FundPage:

    selectStatus_xpath = "//select[@id='status']"
    txtDate_xpath = "//input[@id='reportrange']"
    btnSearch_xpath = "//button[@name='filter']"
    btnAction_xpath = "//table[@id='tableData']/tbody/tr/td[11]"
    textareaRemarks_name = "finalremarks"
    btnApproverd_xpath = "//div[@class='row']/div[5]/div/div[2]/input"
    btnSave_xpath = "//button[@class='btn btn-primary border border-primary-600 text-md px-56 py-12 radius-8']"
    btnAddFundRequest_xpath = "//a[@href='https://b2b.digifintel.com/fundrequest/create']"
    selectTransactionMode_xpath = "//select[@id='transactionmode']"
    txtAmount_xpath = "//input[@name='amount']"
    txtRefrenceID_xpath = "//input[@name='bankutr']"
    txtDepositeDate_xpath = "//input[@name='depositdate']"
    uploadSlip_xpath = "//input[@name='depositslip']"
    txtRemarks_xpath = "//input[@name='remarks']"
    btnSave1_xpath = "//div[@class='d-flex align-items-center justify-content-center gap-3']/button"

    def __init__(self,driver):
        self.driver = driver

    def searchFundRequest(self):
        status=Select(self.driver.find_element(By.XPATH,self.selectStatus_xpath))
        status.select_by_visible_text("Pending")
        self.driver.find_element(By.XPATH,self.txtDate_xpath).send_keys("04-08-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()

    def clickonAction(self):
        self.driver.find_element(By.XPATH,self.btnAction_xpath).click()

    def setFundApproval(self):
        self.driver.find_element(By.XPATH,self.textareaRemarks_name).send_keys("Approver for Retailer DEMORETTWO")
        self.driver.find_element(By.XPATH,self.btnApproverd_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

    def clickonAddFundRequest(self):
        self.driver.find_element(By.XPATH,self.btnAddFundRequest_xpath).click()
        mode=Select(self.driver.find_element(By.XPATH,self.selectTransactionMode_xpath))
        mode.select_by_visible_text("IMPS")
        self.driver.find_element(By.XPATH,self.txtAmount_xpath).send_keys("10000")
        self.driver.find_element(By.XPATH,self.txtRefrenceID_xpath).send_keys("2345676543")
        self.driver.find_elemnet(By.XPATH,self.txtDepositeDate_xpath).send_keys("03-08-2026")
        self.driver.find_element(By.XPATH,self.uploadSlip_xpath).send_keys("C://Users//dell//Pictures//Screenshots//img.png")
        self.driver.find_element(By.XPATH,self.txtRemarks_xpath).send_keys("Fund Add")
        self.driver.find_element(By.XPATH,self.btnSave1_xpath).click()