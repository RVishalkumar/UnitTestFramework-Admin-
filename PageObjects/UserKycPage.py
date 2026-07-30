from selenium import webdriver
from selenium.webdriver.common.by import By

class UserKycPage:

    btnAction_xpath = "//table[@id='tableData']/tbody/tr[1]/td[12]"
    btnApproveMAskAadhar_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[1]/div[2]/div[1]/button[1]"
    btnApproveAadharfront_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[2]/div[2]/div[1]/button[1]"
    btnApproveAadharBack_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[3]/div[2]/div[1]/button[1]"
    btnApprovePanCard_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[4]/div[2]/div[1]/button[1]"
    btnRejectShopImg_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[5]/div[2]/div[1]/button[2]"
    btnCancelCheque_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[6]/div[2]/div[1]/button[1]"
    btnVideoKycApprove_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[7]/div/div[1]/button[1]"
    btnGenerateAgreement_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[8]/div/button"
    btnChooseFile_xpath = "//input[@id='superadmin_agreement_file']"
    btnUploadAgreement_xpath = "//div[@class='row gy-4']/div/div/div//form/div/div[9]/div[3]/button"
    btnSave_xpath = "//div[@class='d-flex align-items-center justify-content-center flex-wrap gap-3']/button"
    lnkdropdownAEPSKyc_xpath = "//*[@href='https://b2b.digifintel.com/aeps_kyc']"
    lnkdropdownUserApproval_xpath = "//*[@href='https://b2b.digifintel.com/users/document/approval']"
    lnkCommissionsMenu_xpath = "//*[@id='sidebar-menu']/li[4]"
    lnkdropdownAeps_xpath = "//a[@href='https://b2b.digifintel.com/commission/aeps']"


    def __init__(self,driver):
        self.driver = driver

    def clickonAction(self):
        self.driver.find_element(By.XPATH,self.btnAction_xpath).click()

    def clickonMaskAadhar(self):
        self.driver.find_element(By.XPATH,self.btnApproveMAskAadhar_xpath).click()

    def clickonAadharFront(self):
        self.driver.find_element(By.XPATH,self.btnApproveAadharfront_xpath).click()

    def clickonAadharBack(self):
        self.driver.find_element(By.XPATH,self.btnApproveAadharBack_xpath).click()

    def clickonPanCard(self):
        self.driver.find_element(By.XPATH,self.btnApprovePanCard_xpath).click()

    def clickonShopImg(self):
        self.driver.find_element(By.XPATH,self.btnRejectShopImg_xpath).click()

    def clickonCancelCheque(self):
        self.driver.find_element(By.XPATH,self.btnCancelCheque_xpath).click()

    def clickonVideoKYC(self):
        self.driver.find_element(By.XPATH,self.btnVideoKycApprove_xpath).click()

    def clickonGenerateAgreement(self):
        self.driver.find_element(By.XPATH,self.btnGenerateAgreement_xpath).click()

    def clickonUpdateAgreementManually(self):
        self.driver.find_element(By.XPATH,self.btnChooseFile_xpath).send_keys("C://Users//dell//Pictures//Screenshots//Screenshot 2026-07-28 121238.png")
        self.driver.find_element(By.XPATH,self.btnUploadAgreement_xpath).click()

    def clickonSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
        if "kyc" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_04_UserKycPage_DocumentKYCp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_04_UserKycPage_DocumentKYCf.png")


    def clickondropdownAPESKyc(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownAEPSKyc_xpath).click()
        if "aeps_kyc" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_04_UserKycPage_AEPSKYCp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_04_UserKycPage_AEPSKYCf.png")

    def clickondropdownUserApproval(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownUserApproval_xpath).click()

    def clickonCommissionsMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCommissionsMenu_xpath).click()

    def clickondropdownAeps(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownAeps_xpath).click()

    

