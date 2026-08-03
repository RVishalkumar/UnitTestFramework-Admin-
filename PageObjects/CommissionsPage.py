from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys


from Utilities.wait import Wait


class CommissionsPage:


    btnNewCommission_xpath = "//a[@href='https://b2b.digifintel.com/aeps/commission/create?service=aeps']"
    txtPackagetitle_xpath = "//input[@id='title']"
    dropdownPackageType_xpath = "//select[@id='pkgtype']"
    txtFromAmount_xpath = "//input[@id='fromamount']"
    txtToAmount_xpath = "//input[@id='toamount']"
    txtWhitelabelComm_xpath = "//input[@id='whitelabel']"
    txtMasterDistributorComm_xpath = "//input[@id='mdistributer']"
    txtDistributorComm_xpath = "//input[@id='distributer']"
    txtRetailerComm_xpath = "//input[@id='retailer']"
    btnStatusShow_xpath = "//input[@id='status1']"
    btnSave_xpath = "//div[@class='card h-100 p-0 radius-12']/div/form/div[2]/button"
    btnArrow_xpath = "//button[@data-target-id='collapse2']"
    btnSlab_xpath = "//button[@data-target='collapse2'][1]"
    txtFrom_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[2]"
    txtTo_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[3]"
    dropdownType_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[4]"
    txtWhitelabel_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[5]"
    txtMasterDistrubutor_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[6]"
    txtDistributor_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[7]"
    txtRetailer_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[8]"
    btnSaveAll_xpath = "//button[@class='btn btn-sm btn-primary save-all-slabs-btn me-1']"
    btnAssign_xpath = "//a[@href='https://b2b.digifintel.com/aeps/commission/assign/AEPSPKG657461eb584fb8611785476582']"
    lnkdropdownRecharge_xpath = "//a[@href='https://b2b.digifintel.com/commission/recharge']"
    btnNewCommissionRecharge_xpath = "//a[@href='https://b2b.digifintel.com/recharge/commission/create?service=recharge']"
    dropdownOperator_xpath = "//select[@id='operator']"
    btnSaveRecharge_xpath = "//button[@class='btn btn-primary digiFin_orange_btn']"
    lnkdropdownDMT_xpath = "//a[@href='https://b2b.digifintel.com/commission/dmt']"
    btnAddMarkupDMT_xpath = "//a[@href='https://b2b.digifintel.com/dmt/commission/create?service=dmt']"
    btnSaveDmt_xpath = "//button[@class='btn btn-primary border border-primary-600 text-md px-56 py-12 radius-8']"
    txtfromDMT_xpath ="//div[@id='collapsedmt2']/div/div/table/tbody/tr[1]/td[2]"
    txtToDMT_xpath = "//div[@id='collapsedmt2']/div/div/table/tbody/tr[1]/td[3]"
    dropdownTypeDMT_xpath = "//div[@id='collapsedmt2']/div/div/table/tbody/tr[1]/td[4]"
    txtWhitelabelDMT_xpath = "//div[@id='collapsedmt2']/div/div/table/tbody/tr[1]/td[5]"
    txtMasterDistributorDMT_xpath = "//div[@id='collapsedmt2']/div/div/table/tbody/tr[1]/td[6]"
    txtDistributorDMT_xpath = "//div[@id='collapsedmt2']/div/div/table/tbody/tr[1]/td[7]"
    txtRetailerDMT_xpath = "//div[@id='collapsedmt2']/div/div/table/tbody/tr[1]/td[8]"
    txtRetailerCashback_xpath = "//div[@id='collapsedmt2']/div/div/table/tbody/tr[1]/td[9]"

    lnkdropdownPayout_xpath = "//a[@href='https://b2b.digifintel.com/commission/payout']"
    btnAddMarkUpPayout_xpath = "//a[@href='https://b2b.digifintel.com/payout/commission/create?service=payout']"
    dropdownService_xpath = "//select[@id='type']"
    dropdownTransaction_xpath = "//select[@id='operator']"
    btnSavePayout_xpath = "//button[@class='btn btn-primary digiFin_orange_btn']"
    txtFromPayout_xpath = "//div[@id='collapsepayout2']/div/div/table/tbody/tr[1]/td[2]"
    txtToPayout_xpath = "//div[@id='collapsepayout2']/div/div/table/tbody/tr[1]/td[3]"
    dropdownPackageTypePayout_xpath = "//div[@id='collapsepayout2']/div/div/table/tbody/tr[1]/td[4]"
    dropdownTransactionTypePayout_xpath = "//div[@id='collapsepayout2']/div/div/table/tbody/tr[1]/td[5]"
    txtWhiteLabelPayout_xpath = "//div[@id='collapsepayout2']/div/div/table/tbody/tr[1]/td[7]"
    txtMasterDistributorPayout_xpath = "//div[@id='collapsepayout2']/div/div/table/tbody/tr[1]/td[8]"
    txtDistributorPayout_xpath = "//div[@id='collapsepayout2']/div/div/table/tbody/tr[1]/td[9]"
    txtRetailerPayout_xpath = "//div[@id='collapsepayout2']/div/div/table/tbody/tr[1]/td[10]"
    lnkdropdownBBPS_xpath = "//a[@href='https://b2b.digifintel.com/commission/bbps']"
    btnNewComBbps_xpath = "//a[@href='https://b2b.digifintel.com/bbps/commission/create?service=bbps']"
    dropdownCategory_xpath = "//select[@id='category']"
    btnSaveBbps_xpath = "//button[@class='btn btn-primary border border-primary-600 text-md px-56 py-12 radius-8']"
    dropdownOperatorBbps_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[5]"
    dropdownTypeBbps_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[6]"
    txtWhiteLabelBbps_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[8]"
    txtMasterDistributorBps_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[9]"
    txtDistributorBbps_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[10]"
    txtRetailerBbps_xpath = "//div[@id='collapse2']/div/div/table/tbody/tr[1]/td[11]"
    lnkdropdownCCPayment_xpath = "//a[@href='https://b2b.digifintel.com/commission/ccpayment']"
    btnAddMarkupCCPayment_xpath = "//a[@href='https://b2b.digifintel.com/ccpayment/commission/create?service=ccpayment']"
    btnSaveCCPayment_xpath = "//div[@class='d-flex align-items-center justify-content-center gap-3']/button"
    txtfrmCCPayment_xpath = "//div[@id='collapseccpayment2']/div/div/table/tbody/tr[1]/td[2]"
    lnkdropdownUPI_xpath = "//a[@href='https://b2b.digifintel.com/commission/upi']"
    btnAddMarkupUPI_xpath = "//a[@href='https://b2b.digifintel.com/upipayment/commission/create?service=upi']"
    btnSaveUPI_xpath = "//button[@class='btn btn-primary border border-primary-600 text-md px-56 py-12 radius-8']"
    lnkdropdownPayin_xpath = "//a[@href='https://b2b.digifintel.com/commission/payin']"
    btnAddMarkupPayin_xpath = "//a[@href='https://b2b.digifintel.com/payin/commission/create?service=payin']"
    dropdownPgServer_xpath = "//select[@id='server']"
    dropdownPgPartner_xpath = "//select[@id='pg_partner']"
    dropdownPgTnxMode_xpath = "//select[@id='pg_operator']"
    dropdownPgSattlement_xpath = "//select[@id='pg_settelement']"
    btnSavePayin_xpath = "//button[@class='btn btn-primary border border-primary-600 text-md px-56 py-12 radius-8']"
    lnkdropdownSwiftX_xpath = "//a[@href='https://b2b.digifintel.com/commission/swiftx']"
    btnAddMarkupSwiftX_xpath = "//a[@href='https://b2b.digifintel.com/swiftx/commission/create?service=swiftx']"
    dropdownServiceType_xpath = "//select[@id='type']"
    dropdownTransactionType_xpath = "//select[@id='operator']"
    btnSaveSwiftX_xpath = "//button[@class='btn btn-primary digiFin_orange_btn']"
    lnkSubscriptionsManu_xpath = "//*[@id='sidebar-menu']/li[5]"
    lnkdropdownManagePlans_xpath = "//a[@href='https://b2b.digifintel.com/subscription/plans']"


    def __init__(self,driver):
        self.driver = driver

    def clickonNewCommission(self):
        self.driver.find_element(By.XPATH,self.btnNewCommission_xpath).click()

    def setAddAepsCommission(self):
        self.driver.find_element(By.XPATH,self.txtPackagetitle_xpath).send_keys("Vishal Pack")
        type = Select(self.driver.find_element(By.XPATH,self.dropdownPackageType_xpath))
        type.select_by_visible_text("Percentage")
        self.driver.find_element(By.XPATH,self.txtFromAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.txtToAmount_xpath).send_keys("1000")
        self.driver.find_element(By.XPATH,self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH,self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH,self.txtRetailerComm_xpath).send_keys("0.1")
        self.driver.find_element(By.XPATH,self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

    def clickonArrow(self):
        Wait.wait_for_click(self.driver,(By.XPATH, self.btnArrow_xpath)).click()


    def clickonSlab(self):
        self.driver.find_element(By.XPATH,self.btnSlab_xpath).click()

    def setSlab(self,famount,tamount):
        self.driver.find_element(By.XPATH,self.txtFrom_xpath).send_keys(famount)
        self.driver.find_element(By.XPATH,self.txtTo_xpath).send_keys(tamount)
        type = Select(self.driver.find_element(By.XPATH,self.dropdownType_xpath))
        type.select_by_visible_text("Flat")
        self.driver.find_element(By.XPATH,self.txtWhitelabel_xpath).send_keys("13")
        self.driver.find_element(By.XPATH,self.txtMasterDistrubutor_xpath).send_keys("12")
        self.driver.find_element(By.XPATH,self.txtDistributor_xpath).send_keys("11")
        self.driver.find_element(By.XPATH,self.txtRetailer_xpath).send_keys("10")
        self.driver.find_element(By.XPATH,self.btnSaveAll_xpath).click()
        if "aeps" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_AEPSCommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_AEPSCommissionf.png")

    def clickonAssign(self):
        self.driver.find_element(By.XPATH,self.btnAssign_xpath).click()

    def clickonAssignUser(self):
        rows=self.driver.find_element(By.XPATH,"//table[@class='table bordered-table sm-table mb-0']/tbody/tr")
        for row in rows:
            email = row.find_element(By.XPATH, "./td[4]").text.strip()
            if email == "vrk9407@gmail.com":
                row.find_element(By.XPATH, "./td[1]").click()
                break
        alert = self.driver.find_element(By.XPATH,"//button[@onclick='getAllUsersIds();']")
        alert.click()
        switchalert = self.driver.switch_to.alert
        switchalert.accept()

    def clickondropdownRecharge(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownRecharge_xpath).click()

    def clickonNewCommissionRecharge(self):
        self.driver.find_element(By.XPATH,self.btnNewCommissionRecharge_xpath).click()


    def setNewCommissionRecharge(self):
        self.driver.find_element(By.XPATH,self.txtPackagetitle_xpath).send_keys("Vishal Pack1")
        oper = self.driver.find_element(By.XPATH,self.dropdownOperator_xpath)
        oper.select_by_visible_text("Airtel Digital TV -- DTH  (S3)  [✅] ")
        self.driver.find_element(By.XPATH,self.txtFromAmount_xpath).send_keys("10")
        self.driver.find_element(By.XPATH,self.txtToAmount_xpath).send_keys("100")
        pack_type=Select(self.driver.find_element(By.XPATH,self.dropdownPackageType_xpath))
        pack_type.select_by_visible_text("Percentage")
        self.driver.find_element(By.XPATH,self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH,self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH,self.txtRetailerComm_xpath).send_keys("0.24")
        self.driver.find_element(By.XPATH,self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSaveRecharge_xpath).click()
        if "recharge" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_RechargeCommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_RechargeCommissionf.png")

    def clickondropdownDMT(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownDMT_xpath).click()


    def clickonAddMarkupDMT(self):
        self.driver.find_element(By.XPATH,self.btnAddMarkupDMT_xpath).click()


    def setDMTMarkupCharge(self):
        self.driver.find_element(By.XPATH,self.txtPackagetitle_xpath).send_keys("Vishal Pack2")
        self.driver.find_element(By.XPATH,self.txtFromAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.txtToAmount_xpath).send_keys("1000")
        type=Select(self.driver.find_element(By.XPATH,self.dropdownPackageType_xpath))
        type.select_by_visible_text("Percentage")
        self.driver.find_element(By.XPATH, self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH,self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH,self.txtRetailerComm_xpath).send_keys("0.24")
        self.driver.find_element(By.XPATH,self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSaveDmt_xpath).click()


    def setSlabDMT(self,famount,tamount):
        self.driver.find_element(By.XPATH,self.txtfromDMT_xpath).send_keys(famount)
        self.driver.find_element(By.XPATH,self.txtToDMT_xpath).send_keys(tamount)
        type = Select(self.driver.find_element(By.XPATH,self.dropdownTypeDMT_xpath))
        type.select_by_visible_text("Flat")
        self.driver.find_element(By.XPATH,self.txtWhitelabelDMT_xpath).send_keys("13")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorDMT_xpath).send_keys("12")
        self.driver.find_element(By.XPATH,self.txtDistributorDMT_xpath).send_keys("11")
        self.driver.find_element(By.XPATH,self.txtRetailerDMT_xpath).send_keys("10")
        self.driver.find_element(By.XPATH,self.txtRetailerCashback_xpath).send_keys("5")
        self.driver.find_element(By.XPATH,self.btnSaveAll_xpath).click()
        if "dmt" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_DMTCommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_DMTCommissionf.png")


    def clickondropdownPayout(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownPayout_xpath).click()

    def clickonAddMarkupPayout(self):
        self.driver.find_element(By.XPATH,self.btnAddMarkUpPayout_xpath).click()

    def setPayoutMarkupCharge(self):
        self.driver.find_element(By.XPATH,self.txtPackagetitle_xpath).send_keys("Vishal Pack3")
        self.driver.find_element(By.XPATH,self.txtFromAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.txtToAmount_xpath).send_keys("5000")
        type = Select(self.driver.find_element(By.XPATH, self.dropdownPackageType_xpath))
        type.select_by_visible_text("Percentage")
        service = Select(self.driver.find_element(By.XPATH,self.dropdownService_xpath))
        service.select_by_visible_text("Aeps Settelment")
        transaction = Select(self.driver.find_element(By.XPATH,self.dropdownTransaction_xpath))
        transaction.select_by_visible_text("IMPS")
        self.driver.find_element(By.XPATH, self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH,self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH,self.txtRetailerComm_xpath).send_keys("0.24")
        self.driver.find_element(By.XPATH,self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSavePayout_xpath).click()

    def setSlabPayout(self,famount,tamount):
        self.driver.find_element(By.XPATH,self.txtFromPayout_xpath).send_keys(famount)
        self.driver.find_element(By.XPATH,self.txtToPayout_xpath).send_keys(tamount)
        type = Select(self.driver.find_element(By.XPATH,self.dropdownPackageTypePayout_xpath))
        type.select_by_visible_text("Flat")
        transaction = Select(self.driver.find_element(By.XPATH,self.dropdownTransactionTypePayout_xpath))
        transaction.select_by_visible_text("IMPS")
        self.driver.find_element(By.XPATH,self.txtWhiteLabelPayout_xpath).send_keys("15")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorPayout_xpath).send_keys("14")
        self.driver.find_element(By.XPATH,self.txtDistributorPayout_xpath).send_keys("13")
        self.driver.find_element(By.XPATH,self.txtRetailerPayout_xpath).send_keys("12")
        self.driver.find_element(By.XPATH,self.btnSaveAll_xpath).click()
        if "payout" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_PayoutCommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_PayoutCommissionf.png")

    def clickondropdownBbps(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownBBPS_xpath).click()

    def clickonNewCommissionBbps(self):
        self.driver.find_element(By.XPATH,self.btnNewComBbps_xpath).click()

    def setBBPSCommission(self):
        self.driver.find_element(By.XPATH,self.txtPackagetitle_xpath).send_keys("Vishal Pack4")
        cate=Select(self.driver.find_element(By.XPATH,self.dropdownCategory_xpath))
        cate.select_by_visible_text("BILL PAYMENT")
        oper=Select(self.driver.find_element(By.XPATH,self.dropdownOperator_xpath))
        oper.select_by_visible_text("AIRTEL MOBILE")
        self.driver.find_element(By.XPATH,self.txtFromAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.txtToAmount_xpath).send_keys("1000")
        type=Select(self.driver.find_element(By.XPATH,self.dropdownPackageType_xpath))
        type.select_by_visible_text("Percentage")
        self.driver.find_element(By.XPATH,self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH,self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH,self.txtRetailerComm_xpath).send_keys("0.24")
        self.driver.find_element(By.XPATH,self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSaveBbps_xpath).click()


    def setSlabBbps(self):
        self.driver.find_element(By.XPATH,self.txtFrom_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.txtTo_xpath).send_keys("10000")
        cate=Select(self.driver.find_element(By.XPATH,self.dropdownType_xpath))
        cate.select_by_visible_text("Electricity")
        operator=Select(self.driver.find_element(By.XPATH,self.dropdownOperatorBbps_xpath))
        operator.select_by_visible_text("BSES Yamuna Power Limited Electricity,BBPS")
        type=Select(self.driver.find_element(By.XPATH,self.dropdownTypeBbps_xpath))
        type.select_by_visible_text("Flat")
        self.driver.find_element(By.XPATH,self.txtWhiteLabelBbps_xpath).send_keys("10")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorBps_xpath).send_keys("9")
        self.driver.find_element(By.XPATH,self.txtDistributorBbps_xpath).send_keys("8")
        self.driver.find_element(By.XPATH,self.txtRetailerBbps_xpath).send_keys("4")
        self.driver.find_element(By.XPATH,self.btnSaveAll_xpath).click()
        if "bbps" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_BBPSCommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_BBPSCommissionf.png")

    def clickonPopUp(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()

    def dropdownCCPayment(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownCCPayment_xpath).click()

    def clickonAddMarkupCCPayment(self):
        self.driver.find_element(By.XPATH,self.btnAddMarkupCCPayment_xpath).click()


    def setCreateCCPaymentCharge(self):
        self.driver.find_element(By.XPATH,self.txtPackagetitle_xpath).send_keys("Vishal CC")
        self.driver.find_element(By.XPATH,self.txtFromAmount_xpath).send_keys("1000")
        self.driver.find_element(By.XPATH,self.txtToAmount_xpath).send_keys("10000")
        type=Select(self.driver.find_element(By.XPATH,self.dropdownPackageType_xpath))
        type.select_by_visible_text("Percentage")
        self.driver.find_element(By.XPATH,self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH,self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH,self.txtRetailerComm_xpath).send_keys("0.24")
        self.driver.find_element(By.XPATH,self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSaveCCPayment_xpath).click()
        if "ccpayment" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_CCPaymentCommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_CCPaymentCommissionf.png")


    def clickondropdownUPI(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownUPI_xpath).click()

    def clickonAddMarkupUPI(self):
        self.driver.find_element(By.XPATH,self.btnAddMarkupUPI_xpath).click()

    def setAddMarkupUPI(self):
        self.driver.find_element(By.XPATH,self.txtPackagetitle_xpath).send_keys("Vishal UPI")
        self.driver.find_element(By.XPATH,self.txtFromAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.txtToAmount_xpath).send_keys("10000")
        type=Select(self.driver.find_element(By.XPATH,self.dropdownPackageType_xpath))
        type.select_by_visible_text("Percentage")
        self.driver.find_element(By.XPATH,self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH,self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH,self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH,self.txtRetailerComm_xpath).send_keys("0.24")
        self.driver.find_element(By.XPATH,self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSaveUPI_xpath).click()
        if "upi" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_UPICommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_UPICommissionf.png")



    def clickondropdownPayin(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownPayin_xpath).click()

    def clickonAddMarkupPayin(self):
        self.driver.find_element(By.XPATH,self.btnAddMarkupPayin_xpath).click()

    def setPayinCharge(self):
        self.driver.find_element(By.XPATH,self.txtPackagetitle_xpath).send_keys("Vishal Payin")
        pg_server=Select(self.driver.find_element(By.XPATH,self.dropdownPgServer_xpath))
        pg_server.select_by_visible_text("SERVER1")
        pg_partner=Select(self.driver.find_element(By.XPATH,self.dropdownPgPartner_xpath))
        pg_partner.select_by_visible_text("RAZORPAYWALLET")
        pg_tnxmode=Select(self.driver.find_element(By.XPATH,self.dropdownPgTnxMode_xpath))
        pg_tnxmode.select_by_visible_text("WALLET")
        pg_sattlement=Select(self.driver.find_element(By.XPATH,self.dropdownPgSattlement_xpath))
        pg_sattlement.select_by_visible_text("Instant")
        self.driver.find_element(By.XPATH,self.txtFromAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.txtToAmount_xpath).send_keys("100000")
        type=Select(self.driver.find_element(By.XPATH,self.dropdownPackageType_xpath))
        type.select_by_visible_text("Percentage")
        self.driver.find_element(By.XPATH, self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH, self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH, self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH, self.txtRetailerComm_xpath).send_keys("0.24")
        self.driver.find_element(By.XPATH,self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSavePayin_xpath).click()
        if "payin" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_payinCommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_payinCommissionf.png")

    def clickondropdownSwiftX(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownSwiftX_xpath).click()

    def clickonAddMarkupSwiftX(self):
        self.driver.find_element(By.XPATH,self.btnAddMarkupSwiftX_xpath).click()

    def setSwiftXMarkUpCharge(self):
        self.driver.find_element(By.XPATH, self.txtPackagetitle_xpath).send_keys("Vishal SwiftX")
        self.driver.find_element(By.XPATH, self.txtFromAmount_xpath).send_keys("1000")
        self.driver.find_element(By.XPATH, self.txtToAmount_xpath).send_keys("25000")
        type = Select(self.driver.find_element(By.XPATH, self.dropdownPackageType_xpath))
        type.select_by_visible_text("Percentage")
        service_type=Select(self.driver.find_element(By.XPATH,self.dropdownServiceType_xpath))
        service_type.select_by_visible_text("Swiftx")
        tran_type=Select(self.driver.find_element(By.XPATH,self.dropdownTransactionType_xpath))
        tran_type.select_by_visible_text("IMPS")
        self.driver.find_element(By.XPATH, self.txtWhitelabelComm_xpath).send_keys("0.37")
        self.driver.find_element(By.XPATH, self.txtMasterDistributorComm_xpath).send_keys("0.35")
        self.driver.find_element(By.XPATH, self.txtDistributorComm_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH, self.txtRetailerComm_xpath).send_keys("0.1")
        self.driver.find_element(By.XPATH, self.btnStatusShow_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSaveSwiftX_xpath).click()
        if "swiftx" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_CommissionPage_SwiftxCommissionp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_CommissionPage_SwiftxCommissionf.png")


    def clickonSubscriptionsMenu(self):
        self.driver.find_element(By.XPATH,self.lnkSubscriptionsManu_xpath).click()

    def clickondropdownManagePlans(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownManagePlans_xpath).click()

