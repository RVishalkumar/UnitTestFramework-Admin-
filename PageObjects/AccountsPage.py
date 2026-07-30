from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AccountsPage:

    selectRole_xpath = "//select[@id='roleid']"
    textRetailer_xpath = "//input[@id='parentid-ts-control']"
    selectStatus_xpath = "//select[@id='status']"
    btnSearch_xpath = "//button[@name='filter']"
    btnReset_xpath = "//div[@class='row manageProfile_filter']/div[6]/a"
    btnAddNewUser_xpath = "//div[@class='d-flex flex-wrap align-items-center gap-3 manage_user_add_count mt-3 mt-lg-0']/a[1]"
    dropdownRole_xpath = "//select[@id='role']"
    txtFirstName_name = "fname"
    txtLastNAme_name = "lname"
    txtEmail_name = "email"
    txtMobile_name = "mobile"
    txtPassword_name = "password"
    txtDOB_name = "dateofbirth"
    selectAssignDMTPackage_xpath = "//select[@id='dmt_package']"
    selectRechargePackage_xpath = "//select[@id='rec_package']"
    selectAEPSPackage_xpath = "//select[@id='aeps_package']"
    selectBBPSPackage_xpath = "//select[@id='bbps_package']"
    selectPayoutPackage_xpath = "//select[@id='payout_package']"
    selectCCPayPackage_xpath = "//select[@id='ccpay_package']"
    selectPayinPackage_xpath = "//select[@id='payin_package']"
    selectUPIPackage_xpath = "//select[@id='upi_package']"
    selectSwiftXPackage_xpath = "//select[@id='swiftx_package']"
    txtAAdharNumner_name = "aadharnumber"
    txtPanCardNumber_xpath = "//input[@id='pancardnumber']"
    txtDomain_name = "domain"
    txtBrandName_name = "brand_name"
    txtCompanyRegisterName_name = "com_leagal_name"
    txtSupportEmail_name = "support_email"
    txtSupportMobile_name = "support_mobile"
    imgCompanyLogo_name = "logoimg"
    imgCompanyFavicon_name = "faviconimg"
    imgCancelCheck_name = "chequeimg"
    btnStatus_xpath = "//input[@id='status1']"
    btnCreateUser_xpath = "//button[@class='btn btn-primary digiFin_orange_btn']"
    lnkUserKYCMenu_xpath = "//*[@id='sidebar-menu']/li[3]"
    lnkdropdownDocumentKYC_xpath = "//*[@href='https://b2b.digifintel.com/users/document/kyc']"

    def __init__(self,driver):
        self.driver = driver

    def selectRoles(self):
        role = Select(self.driver.find_element(By.XPATH,self.selectRole_xpath))
        role.select_by_visible_text("Retailer")

    def setRetailer(self):
        self.driver.find_element(By.XPATH,self.textRetailer_xpath).send_keys("Vishal test (DEMORT00017)")

    def selectStatus(self):
        status = Select(self.driver.find_element(By.XPATH,self.selectStatus_xpath))
        status.select_by_visible_text("Active")

    def clickonSearch(self):
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()

    def clickonReset(self):
        self.driver.find_element(By.XPATH,self.btnReset_xpath).click()

    def clickonAddNewUser(self):
        self.driver.find_element(By.XPATH,self.btnAddNewUser_xpath).click()

    def setAddUser(self):
        role=Select(self.driver.find_element(By.XPATH,self.dropdownRole_xpath))
        role.select_by_visible_text(" whitelabel")
        self.driver.find_element(By.NAME,self.txtFirstName_name).send_keys("Vishal")
        self.driver.find_element(By.NAME,self.txtLastNAme_name).send_keys("Kumar")
        self.driver.find_element(By.NAME,self.txtEmail_name).send_keys("vrk9407@gmail.com")
        self.driver.find_element(By.NAME,self.txtMobile_name).send_keys("9407271094")
        self.driver.find_element(By.NAME,self.txtPassword_name).send_keys("Test@@123")
        self.driver.find_element(By.NAME,self.txtDOB_name).send_keys("14-10-1998")
        dmt=Select(self.driver.find_element(By.XPATH,self.selectAssignDMTPackage_xpath))
        dmt.select_by_visible_text("test")
        recharge=Select(self.driver.find_element(By.XPATH,self.selectRechargePackage_xpath))
        recharge.select_by_visible_text(" PERCENT wala NAYA")
        aeps=Select(self.driver.find_element(By.XPATH,self.selectAEPSPackage_xpath))
        aeps.select_by_visible_text("test")
        bbps=Select(self.driver.find_element(By.XPATH,self.selectBBPSPackage_xpath))
        bbps.select_by_visible_text("tomb bbps")
        payout=Select(self.driver.find_element(By.XPATH,self.selectPayoutPackage_xpath))
        payout.select_by_visible_text("demo test")
        ccpay=Select(self.driver.find_element(By.XPATH,self.selectCCPayPackage_xpath))
        ccpay.select_by_visible_text("package wala")
        payin=Select(self.driver.find_element(By.XPATH,self.selectPayinPackage_xpath))
        payin.select_by_visible_text("best")
        upi=Select(self.driver.find_element(By.XPATH,self.selectUPIPackage_xpath))
        upi.select_by_visible_text("chai")
        swift=Select(self.driver.find_element(By.XPATH,self.selectSwiftXPackage_xpath))
        swift.select_by_visible_text("PLAN WALA")
        self.driver.find_element(By.NAME,self.txtAAdharNumner_name).send_keys("452041019120")
        self.driver.find_element(By.XPATH,self.txtPanCardNumber_xpath).send_keys("BLFPK0735B")
        self.driver.find_element(By.NAME,self.txtDomain_name).send_keys("www.paisabhejo.com")
        self.driver.find_element(By.NAME,self.txtBrandName_name).send_keys("PB")
        self.driver.find_element(By.NAME,self.txtCompanyRegisterName_name).send_keys("PaisaBhejo")
        self.driver.find_element(By.NAME,self.txtSupportEmail_name).send_keys("paisabhejo@gmail.com")
        self.driver.find_element(By.NAME,self.txtSupportMobile_name).send_keys("9631312967")
        self.driver.find_element(By.NAME,self.imgCompanyLogo_name).send_keys("C://Users//dell//Pictures//Screenshots//Screenshot 2026-07-28 121434.png")
        self.driver.find_element(By.NAME,self.imgCompanyFavicon_name).send_keys("C://Users//dell//Pictures//Screenshots//Screenshot 2026-05-28 162658.png")
        self.driver.find_element(By.NAME,self.imgCancelCheck_name).send_keys("C://Users//dell//Pictures//Screenshots//Screenshot 2026-05-30 001441.png")
        self.driver.find_element(By.XPATH,self.btnStatus_xpath).click()
        self.driver.find_element(By.XPATH,self.btnCreateUser_xpath).click()

    def clickonUserKYCMenu(self):
        self.driver.find_element(By.XPATH,self.lnkUserKYCMenu_xpath).click()

    def clickondropdownDocumentKYC(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownDocumentKYC_xpath).click()
