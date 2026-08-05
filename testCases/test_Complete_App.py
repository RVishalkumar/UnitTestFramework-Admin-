import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from PageObjects.AmountThresholdPage import AmountThresholdPage
from PageObjects.CommissionsPage import CommissionsPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.FundPage import FundPage
from PageObjects.LoginPage import LoginPage
from PageObjects.AccountsPage import AccountsPage
from PageObjects.ManageLeadsPage import ManageLeadsPage
from PageObjects.MerchantEnquiryPage import MerchantEnquiryPage
from PageObjects.ReportsPage import ReportsPage
from PageObjects.SalesTeamPage import SalesTeamPage
from PageObjects.ServicePanelPage import ServicePanelPage
from PageObjects.SettingsPage import SettingsPage
from PageObjects.SinUpPage import SinUpPage
from PageObjects.SubscriptionsPage import SubscriptionsPage
from PageObjects.TeamsPage import TeamsPage
from PageObjects.UserKycPage import UserKycPage
from PageObjects.VerificationPanelPage import VerificationPanelPage
from PageObjects.WalletPassbookPage import WalletPassbookPage
from Utilities.readProperties import ReadConfig

class Test_01_Complete_App(unittest.TestCase):

    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()


    @classmethod
    def setUpClass(cls):
        service_obj = Service("C://Users//dell//Desktop//chromedriver.exe")
        global driver
        driver = webdriver.Chrome(service=service_obj)
        driver.get(cls.baseurl)
        driver.maximize_window()
        driver.implicitly_wait(5)


    def test_01_loginPages(self):
        self.lp = LoginPage(driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        #self.lp.clickonView()
        time.sleep(3)
        self.lp.clickLogin()
        self.lp.setOTP1(1)
        self.lp.setOTP2(2)
        self.lp.setOTP3(3)
        self.lp.setOTP4(4)
        self.lp.setOTP5(5)
        self.lp.setOTP6(6)
        self.lp.clickonContinue()
        self.lp.clickonPopUp()

    def test_02_DashboardPage(self):
        self.dp = DashboardPage(driver)
        self.dp.clickonWallet()
        self.dp.clickonMode()
        self.dp.clickonMode()
        self.dp.clickonNotification()
        self.dp.clickonProfileImage()
        self.dp.clickonProfileTag()
        self.dp.clickonProfileImage()
        self.dp.clickonChangePassword()
        self.dp.clickonProfileImage()
        self.dp.clickonSettings()
        self.dp.clickonAccountsMenu()

    def test_03_AccountsPage(self):
        self.ap = AccountsPage(driver)
        self.ap.selectRoles()
        self.ap.setRetailer()
        self.ap.selectStatus()
        self.ap.clickonSearch()
        #self.ap.clickonReset()
        self.ap.clickonAddNewUser()
        self.ap.setAddUser()
        self.ap.clickonUserKYCMenu()
        self.ap.clickondropdownDocumentKYC()

    def test_04_UserKycPage(self):
        self.ukp = UserKycPage(driver)
        self.ukp.clickonAction()
        self.ukp.clickonMaskAadhar()
        self.ukp.clickonAadharFront()
        self.ukp.clickonAadharBack()
        self.ukp.clickonPanCard()
        self.ukp.clickonShopImg()
        self.ukp.clickonCancelCheque()
        self.ukp.clickonVideoKYC()
        self.ukp.clickonGenerateAgreement()
        self.ukp.clickonUpdateAgreementManually()
        self.ukp.clickonSave()
        self.ukp.clickondropdownAPESKyc()

    def test_05_CommissionsPage(self):
        self.cp = CommissionsPage(driver)
        self.cp.clickonNewCommission()
        self.cp.setAddAepsCommission()
        self.cp.clickonArrow()
        self.cp.clickonSlab()
        self.cp.setSlab(101,1000)
        self.cp.clickonPopUp()
        self.cp.clickonAssign()
        self.cp.clickonAssignUser()
        self.cp.clickondropdownRecharge()
        self.cp.clickonNewCommissionRecharge()
        self.cp.setNewCommissionRecharge()
        self.cp.clickonAssign()
        self.cp.clickonAssignUser()
        self.cp.clickondropdownDMT()
        self.cp.clickonAddMarkupDMT()
        self.cp.setDMTMarkupCharge()
        self.cp.clickonArrow()
        self.cp.clickonSlab()
        self.cp.setSlabDMT(1001,5000)
        self.cp.clickonPopUp()
        self.cp.clickonAssign()
        self.cp.clickonAssignUser()
        self.cp.clickondropdownPayout()
        self.cp.clickonAddMarkupPayout()
        self.cp.setPayoutMarkupCharge()
        self.cp.clickonArrow()
        self.cp.clickonSlab()
        self.cp.setSlabPayout(5001,6000)
        self.cp.clickonPopUp()
        self.cp.clickonAssign()
        self.cp.clickonAssignUser()
        self.cp.clickondropdownBbps()
        self.cp.clickonNewCommissionBbps()
        self.cp.setBBPSCommission()
        self.cp.setSlabBbps()
        self.cp.clickonPopUp()
        self.cp.dropdownCCPayment()
        self.cp.clickonAddMarkupCCPayment()
        self.cp.setCreateCCPaymentCharge()
        self.cp.clickonAssign()
        self.cp.clickonAssignUser()
        self.cp.clickondropdownUPI()
        self.cp.clickonAddMarkupUPI()
        self.cp.setAddMarkupUPI()
        self.cp.clickonAssign()
        self.cp.clickonAssignUser()
        self.cp.clickondropdownPayin()
        self.cp.clickonAddMarkupPayin()
        self.cp.setPayinCharge()
        self.cp.clickonAssign()
        self.cp.clickonAssignUser()
        self.cp.clickondropdownSwiftX()
        self.cp.clickonAddMarkupSwiftX()
        self.cp.setSwiftXMarkUpCharge()
        self.cp.clickonAssign()
        self.cp.clickonAssignUser()
        self.cp.clickonSubscriptionsMenu()
        self.cp.clickondropdownManagePlans()

    def test_06_SubscriptionsPage(self):
        self.sp = SubscriptionsPage(driver)
        self.sp.captureManagePlans()
        self.sp.clickonCreatePlans()
        self.sp.setSubscriptionsPlan()
        self.sp.setReferralDistributorCommission()
        self.sp.clickonSubmit()
        self.sp.setCommissionPackageOverride()
        self.sp.clickonReportMenu()
        self.sp.clickondropdownLadgerReports()

    def test_07_ReportsPage(self):
        self.rp = ReportsPage(driver)
        self.rp.searchLadgerReports()
        self.rp.clickonAEPSReports()
        self.rp.searchAEPSReports()
        self.rp.clickonDMTReports()
        self.rp.searchDMTReports()
        self.rp.clickonPayoutReports()
        self.rp.searchPayoutReports()
        self.rp.clickonRechargeReports()
        self.rp.searchRechargeReports()
        self.rp.clickonBBPSReports()
        self.rp.searchBBPSReports()
        self.rp.clickonCCPayReports()
        self.rp.searchCCPayReports()
        self.rp.clickonUPIReports()
        self.rp.searchUPIReports()
        self.rp.clickonPayinReports()
        self.rp.searchPayinReports()
        self.rp.clickonSwiftXReports()
        self.rp.searchSwiftXReports()
        self.rp.clickonFundMenu()
        self.rp.clickondropdownFundRequest()


    def test_08_FundPage(self):
        self.fp = FundPage(driver)
        self.fp.searchFundRequest()
        self.fp.clickonAction()
        self.fp.setFundApproval()
        self.fp.clickonAddFundRequest()
        self.fp.clickondropdownCreditPayment()
        self.fp.setCreditFund()
        self.fp.clickondropdownDebitPayment()
        self.fp.clickonSettingsMenu()
        self.fp.clickondropdownAllBanner()

    def test_09_SettingsPage(self):
        self.sp = SettingsPage(driver)
        self.sp.setBanners()
        self.sp.clickondropdownNotificationAlerts()
        self.sp.clickonAddNotification()
        self.sp.setAddNotifications()
        self.sp.clickondropdownMasterBank()
        self.sp.clickonAddNewBank()
        self.sp.setAddBank()
        self.sp.clickondropdownServiceGateway()
        self.sp.clickonAddServiceGateway()
        self.sp.setAddServiceGateway()
        self.sp.clickonTeamsMenu()

    def test_10_TeamsPage(self):
        self.tp = TeamsPage(driver)
        self.tp.clickonAddNewTeams()
        self.tp.setAddTeam()
        self.tp.setManageTeams()
        self.tp.setAllowPermissions()
        self.sp = SettingsPage(driver)
        self.sp.clickonTeamsMenu()
        self.tp.clickonSalesTeamsMenu()

    def test_11_SalesTeamsPage(self):
        self.stp = SalesTeamPage(driver)
        self.stp.clickonAddNewUser()
        self.stp.setAddTeam()
        self.stp.clickonServicePanelMenu()

    def test_12_ServicePanelPage(self):
        self.spp = ServicePanelPage(driver)
        self.spp.controlCMSServicePanel()
        self.spp.controlPayoutServicePanel()
        self.spp.clickonWalletPassbookMenu()

    def test_13_WalletPassbookPage(self):
        self.wpp = WalletPassbookPage(driver)
        self.wpp.searchRetailerWalletPassbook()
        self.wpp.clickonVerificationPanelMenu()

    def test_14_VerificationPanelPage(self):
        self.vpp = VerificationPanelPage(driver)
        self.vpp.clickonManageLeadsMenu()


    def test_15_ManageLeadsPage(self):
        self.mlp = ManageLeadsPage(driver)
        self.mlp.clickonAmountThreshold()


    def test_16_AmountThresholdPage(self):
        self.amtp = AmountThresholdPage(driver)
        self.amtp.setAmountThreshold()
        self.amtp.clickonMerchantEnquiryMenu()

    def test_17_MerchantEnquiryPage(self):
        self.mep = MerchantEnquiryPage(driver)
        self.mep.searchMerchantList()
        self.mep.clickonTransactionStatusMenu()










    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Passed")
        driver.quit()

if __name__ == "__main__":
    unittest.main()
