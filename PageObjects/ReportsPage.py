from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




class ReportsPage:

    selectRole_xpath = "//select[@id='roleid']"
    selectRetailers_xpath = "//select[@id='parentid']"
    selectStatus_xpath = "//select[@id='status']"
    txtDate_xpath = "//input[@id='reportrange']"
    btnSearch_xpath = "//div[@class='form-group col-lg-4 ledger_report_searchBtn']/input"
    lnkdropdownAEPSReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/aeps']"
    lnkdropdownDMTReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/dmt']"
    lnkdropdownPayoutReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/payout']"
    lnkdropdownRechargeReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/recharge']"
    lnkdropdownBBPSReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/bbps']"
    lnkdropdownCCPayReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/ccpay']"
    lnkdropdownUPIReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/upi']"
    lnkdropdownPayinReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/payin']"
    lnkdropdownSwiftxReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/swiftx']"
    lnkFundMenu_xpath = "//*[@id='sidebar-menu']/li[7]"
    lnkdropdownFundRequest_xpath = "//a[@href='https://b2b.digifintel.com/fundrequest']"

    def __init__(self,driver):
        self.driver = driver

    def searchLadgerReports(self):
        role=Select(self.driver.find_element(By.XPATH,self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret=Select(self.driver.find_element(By.XPATH,self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status=Select(self.driver.find_element(By.XPATH,self.selectStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH,self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()
        if "ledger" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_LadgerReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_LadgerReportsf.png")

    def clickonAEPSReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownAEPSReports_xpath).click()


    def searchAEPSReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH,self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()
        if "aeps" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_AEPSReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_AEPSReportsf.png")

    def clickonDMTReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownDMTReports_xpath).click()


    def searchDMTReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Failed")
        self.driver.find_element(By.XPATH, self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        if "dmt" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_DMTReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_DMTReportsf.png")

    def clickonPayoutReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownPayoutReports_xpath).click()

    def searchPayoutReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Failed")
        self.driver.find_element(By.XPATH, self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        if "payout" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_PayoutReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_PayoutReportsf.png")

    def clickonRechargeReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownRechargeReports_xpath).click()

    def searchRechargeReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH, self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        if "recharge" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_RechargeReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_RechargeReportsf.png")

    def clickonBBPSReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownBBPSReports_xpath).click()

    def searchBBPSReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH, self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        if "bbps" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_BBPSReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_BBPSReportsf.png")

    def clickonCCPayReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownCCPayReports_xpath).click()

    def searchCCPayReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Failed")
        self.driver.find_element(By.XPATH, self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        if "ccpay" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_CCPayReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_CCPayReportsf.png")


    def clickonUPIReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownUPIReports_xpath).click()


    def searchUPIReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH, self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        if "upi" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_UPIReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_UPIReportsf.png")

    def clickonPayinReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownPayinReports_xpath).click()

    def searchPayinReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH, self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        if "payin" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_PayinReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_PayinReportsf.png")

    def clickonSwiftXReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownSwiftxReports_xpath).click()

    def searchSwiftXReports(self):
        role = Select(self.driver.find_element(By.XPATH, self.selectRole_xpath))
        role.select_by_visible_text("Retailer")
        ret = Select(self.driver.find_element(By.XPATH, self.selectRetailers_xpath))
        ret.select_by_visible_text("DEMO RET TWO (DEMORT00002 - RT)")
        status = Select(self.driver.find_element(By.XPATH, self.selectStatus_xpath))
        status.select_by_visible_text("Failed")
        self.driver.find_element(By.XPATH, self.txtDate_xpath).send_keys("04-07-2026 - 03-08-2026")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        if "swiftx" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_ReportsPage_SwiftXReportsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_ReportsPage_SwiftXReportsf.png")


    def clickonFundMenu(self):
        self.driver.find_element(By.XPATH,self.lnkFundMenu_xpath).click()


    def clickondropdownFundRequest(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownFundRequest_xpath).click()

