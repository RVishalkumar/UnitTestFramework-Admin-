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
    selectBank_xpath = "//select[@id='bankid']"
    txtAmount_xpath = "//input[@name='amount']"
    txtRefrenceID_xpath = "//input[@name='bankutr']"
    txtDepositeDate_xpath = "//input[@name='depositdate']"
    uploadSlip_xpath = "//input[@name='depositslip']"
    txtRemarks_xpath = "//input[@name='remarks']"
    btnSave1_xpath = "//div[@class='d-flex align-items-center justify-content-center gap-3']/button"
    lnkdropdownCreditPayment = "//a[@href='https://b2b.digifintel.com/fund/credit/payment']"
    selectRolesCredit_xpath = "//select[@id='roleid']"
    selectRetailerName_xpath = "//select[@id='parentid']"
    txtAmountCreditPayment_xpath = "//input[@id='amount']"
    txtTransactionPin_xpath = "//input[@id='txnpin']"
    txtareaRemark_xpath = "//textarea[@id='message']"
    btnSave2_xpath = "//button[@id='saveButton']"
    lnkdropdownDebitPayment_xpath = "//a[@href='https://b2b.digifintel.com/fund/debit/payment']"
    btnSave3_xpath = "//button[@id='savedebitButton']"
    lnkSettingsMenu_xpath = "//*[@id='sidebar-menu']/li[8]"
    lnkdropdownAllBanner_xpath = "//a[@href='https://b2b.digifintel.com/slider']"

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
        bank=Select(self.driver.find_element(By.XPATH,self.selectBank_xpath))
        bank.select_by_visible_text("Newgenguru Private Limited || ICICI Bank || 414501505371 || ICIC0004145 [DigiFintel Super (superadmin)]")
        self.driver.find_element(By.XPATH,self.txtAmount_xpath).send_keys("10000")
        self.driver.find_element(By.XPATH,self.txtRefrenceID_xpath).send_keys("2345676543")
        self.driver.find_elemnet(By.XPATH,self.txtDepositeDate_xpath).send_keys("03-08-2026")
        self.driver.find_element(By.XPATH,self.uploadSlip_xpath).send_keys("C://Users//dell//Pictures//Screenshots//img.png")
        self.driver.find_element(By.XPATH,self.txtRemarks_xpath).send_keys("Fund Add")
        self.driver.find_element(By.XPATH,self.btnSave1_xpath).click()

    def clickondropdownCreditPayment(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownCreditPayment).click()

    def setCreditFund(self):
        role=Select(self.driver.find_element(By.XPATH,self.selectRolesCredit_xpath))
        role.select_by_visible_text("Retailer")
        retailer=Select(self.driver.find_element(By.XPATH,self.selectRetailerName_xpath))
        retailer.select_by_visible_text("Vishal test (DEMORT00017)")
        self.driver.find_element(By.XPATH,self.txtAmountCreditPayment_xpath).send_keys("200000")
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.txtareaRemark_xpath).send_keys("Fund Credit")
        self.driver.find_element(By.XPATH,self.btnSave2_xpath).click()

    def clickondropdownDebitPayment(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownDebitPayment_xpath).click()
        role = Select(self.driver.find_element(By.XPATH, self.selectRolesCredit_xpath))
        role.select_by_visible_text("Retailer")
        retailer = Select(self.driver.find_element(By.XPATH, self.selectRetailerName_xpath))
        retailer.select_by_visible_text("DEMO RET TWO (DEMORT00002)")
        self.driver.find_element(By.XPATH, self.txtAmountCreditPayment_xpath).send_keys("10000")
        self.driver.find_element(By.XPATH, self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.txtareaRemark_xpath).send_keys("Fund Debit")
        self.driver.find_element(By.XPATH,self.btnSave3_xpath).click()


    def clickonSettingsMenu(self):
        self.driver.find_element(By.XPATH,self.lnkSettingsMenu_xpath).click()

    def clickondropdownAllBanner(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownAllBanner_xpath).click()


    


