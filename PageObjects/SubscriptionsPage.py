from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SubscriptionsPage:

    btnCreatePlan_xpath = "//div[@class='row gy-4']/div/div/div/div/a"
    btnEnterprises_xpath = "//div[@class='plan-type-cards']/label[3]"
    txtCustomerPlanName_xpath = "//input[@name='custom_name']"
    txt1monthPeriod_xpath = "//input[@name='price_1m']"
    txt1monthDiscount_xpath = "//input[@name='discount_1m']"
    txt3monthsPeriod_xpath = "//input[@name='price_3m']"
    txt3monthsDiscount_xpath = "//input[@name='discount_3m']"
    txt6monthsPeriod_xpath = "//input[@name='price_6m']"
    txt6monthsDiscount_xpath = "//input[@name='discount_6m']"
    txt9monthsPeriod_xpath = "//input[@name='price_9m']"
    txt9monthsDiscount_xpath = "//input[@name='discount_9m']"
    txt12monthsPeriod_xpath = "//input[@name='price_12m']"
    txt12monthsDiscount_xpath = "//input[@name='discount_12m']"
    txtReferralDistributorCom_xpath = "//input[@name='ref_dt_commission']"
    btnSubmitCreatePlan_xpath = "//button[@id='submitBtn']"
    selectAEPSPackage_xpath = "//select[@id='pkg-select-aeps']"
    selectDMTPackage_xpath = "//select[@id='pkg-select-dmt']"
    selectPayoutPackage_xpath = "//select[@id='pkg-select-payout']"
    selectBBPSPackage_xpath = "//select[@id='pkg-select-bbps']"
    selectRechargePackage_xpath = "//select[@id='pkg-select-recharge']"
    selectPayinPackage_xpath = "//select[@id='pkg-select-payin']"
    selectUPIPackage_xpath = "//select[@id='pkg-select-upi']"
    selectCCPayPackage_xpath = "//select[@id='pkg-select-ccpay']"
    selectSwiftXPackage_xpath = "//select[@id='pkg-select-swiftx']"
    lnkReportMenu_xpath = "//*[@id='sidebar-menu']/li[6]"
    lnkdropdownLadgerReports_xpath = "//a[@href='https://b2b.digifintel.com/reports/ledger']"



    def __init__(self,driver):
        self.driver = driver

    def captureManagePlans(self):
        if "plans" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_06_SubscriptionsPage_ManagePlansp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_06_SubscriptionsPage_ManagePlansf.png")

    def clickonCreatePlans(self):
        self.driver.find_element(By.XPATH,self.btnCreatePlan_xpath).click()

    def setSubscriptionsPlan(self):
        self.driver.find_element(By.XPATH,self.btnEnterprises_xpath).click()
        self.driver.find_element(By.XPATH,self.txtCustomerPlanName_xpath).send_keys("Platinum")
        self.driver.find_element(By.XPATH,self.txt1monthPeriod_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt1monthPeriod_xpath).send_keys("199")
        self.driver.find_element(By.XPATH,self.txt1monthDiscount_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt1monthDiscount_xpath).send_keys("-2")
        self.driver.find_element(By.XPATH,self.txt3monthsPeriod_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt3monthsPeriod_xpath).send_keys("599")
        self.driver.find_element(By.XPATH,self.txt3monthsDiscount_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt3monthsDiscount_xpath).send_keys("-2")
        self.driver.find_element(By.XPATH,self.txt6monthsPeriod_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt6monthsPeriod_xpath).send_keys("999")
        self.driver.find_element(By.XPATH,self.txt6monthsDiscount_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt6monthsDiscount_xpath).send_keys("-2")
        self.driver.find_element(By.XPATH,self.txt9monthsPeriod_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt9monthsPeriod_xpath).send_keys("1199")
        self.driver.find_element(By.XPATH,self.txt9monthsDiscount_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt9monthsDiscount_xpath).send_keys("-2")
        self.driver.find_element(By.XPATH,self.txt12monthsPeriod_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt12monthsPeriod_xpath).send_keys("1299")
        self.driver.find_element(By.XPATH,self.txt12monthsDiscount_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt12monthsDiscount_xpath).send_keys("-1")

    def setReferralDistributorCommission(self):
        self.driver.find_element(By.XPATH,self.txtReferralDistributorCom_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtReferralDistributorCom_xpath).send_keys("2")


    def clickonSubmit(self):
        self.driver.find_element(By.XPATH,self.btnSubmitCreatePlan_xpath).click()

    def setCommissionPackageOverride(self):
        aeps=Select(self.driver.find_element(By.XPATH,self.selectAEPSPackage_xpath))
        aeps.select_by_visible_text("Vishal Pack")
        dmt=Select(self.driver.find_element(By.XPATH,self.selectDMTPackage_xpath))
        dmt.select_by_visible_text("Vishal Pack2")
        payout=Select(self.driver.find_element(By.XPATH,self.selectPayoutPackage_xpath))
        payout.select_by_visible_text("Vishal Pack3")
        bbps=Select(self.driver.find_element(By.XPATH,self.selectBBPSPackage_xpath))
        bbps.select_by_visible_text("Vishal Pack4")
        recharge=Select(self.driver.find_element(By.XPATH,self.selectRechargePackage_xpath))
        recharge.select_by_visible_text("Vishal Pack1")
        payin=Select(self.driver.find_element(By.XPATH,self.selectPayinPackage_xpath))
        payin.select_by_visible_text("Vishal Payin")
        upi=Select(self.driver.find_element(By.XPATH,self.selectUPIPackage_xpath))
        upi.select_by_visible_text("Vishal UPI")
        ccpay=Select(self.driver.find_element(By.XPATH,self.selectCCPayPackage_xpath))
        ccpay.select_by_visible_text("Vishal CC")
        swiftx=Select(self.driver.find_element(By.XPATH,self.selectSwiftXPackage_xpath))
        swiftx.select_by_visible_text("Vishal SwiftX")


    def clickonReportMenu(self):
        self.driver.find_element(By.XPATH,self.lnkReportMenu_xpath).click()

    def clickondropdownLadgerReports(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownLadgerReports_xpath).click()

        



