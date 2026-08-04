from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SettingsPage:

    txtTitle_name = "title"
    chooseImage_name = "image"
    textareaSummary_xpath = "//textarea[@id='editor']"
    txtDisplayOrder_name = "sortid"
    btnSave_xpath = "//button[@id='submitBtn']"
    lnkdropdownNotificationAlert_xpath = "//a[@href='https://b2b.digifintel.com/notification']"
    btnAddNotificationAlert_xpath = "//a[@href='https://b2b.digifintel.com/notification/create']"
    btnSave1_xpath = "//div[@class='dashboard-main-body']/div[2]/div/div/div/div/div/form/div[2]/button"
    lnkdropdownMasterBank_xpath = "//a[@href='https://b2b.digifintel.com/bankmaster']"
    btnAddNewBank_xpath = "//a[@href='https://b2b.digifintel.com/bankmaster/create']"
    selectType_xpath = "//select[@id='entry_type']"
    txtPayeeNAme_xpath = "//input[@id='payeename']"
    txtBankNAme_xpath = "//input[@id='bankname']"
    txtAccountType_xpath = "//input[@id='accounttype']"
    txtAccountNumber_xpath = "//input[@id='accountnumber']"
    txtIFCcode_xpath = "//input[@id='ifsccode']"
    txtBranchName_xpath = "//input[@id='branchname']"
    btnSaveBank_xpath = "//button[@class='btn btn-primary digiFin_orange_btn']"
    lnkdropdownGateways_xpath = "//a[@href='https://b2b.digifintel.com/service-gateways']"
    btnAddNewGateway_xpath = "//a[@id='createGatewayBtn']"
    dropdownService_xpath = "//select[@id='serviceSelect']"
    dropdownVendor_xpath = "//select[@id='vendorSelect']"
    txtGatewayLimit_xpath = "//div[@id='payinExtraFields']/div[1]/input"
    txtGatewayCategory_xpath = "//div[@id='payinExtraFields']/div[2]/input"
    txtDomesticCardNetwork_xpath = "//div[@id='payinExtraFields']/div[3]/input"
    btnCreateGateway_xpath = "//div[@id='gatewayModalBody']/form/div[2]/button[2]"
    lnkTeamsMenu_xpath = "//*[@id='sidebar-menu']/li[9]"





    def __init__(self,driver):
        self.driver = driver

    def setBanners(self):
        self.driver.find_element(By.NAME,self.txtTitle_name).send_keys("Application Banners")
        self.driver.find_element(By.NAME,self.chooseImage_name).send_keys("C://Users//dell//Pictures//Screenshot//Screenshot 2026-07-30 175224.png")
        self.driver.find_element(By.XPATH,self.textareaSummary_xpath).send_keys("My Application Banner")
        self.driver.find_element(By.NAME,self.txtDisplayOrder_name).send_keys("1")
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
        if "slider" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_09_SettingsPage_Bannersp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_09_SettingsPage_Bannersf.png")


    def clickondropdownNotificationAlerts(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownNotificationAlert_xpath).click()


    def clickonAddNotification(self):
        self.driver.find_element(By.XPATH,self.btnAddNotificationAlert_xpath).click()


    def setAddNotifications(self):
        self.driver.find_element(By.NAME,self.txtTitle_name).send_keys("Vishal Notification")
        self.driver.find_element(By.XPATH,self.textareaSummary_xpath).send_keys("show only in Whitelabe")
        self.driver.find_element(By.NAME,self.btnSave1_xpath).click()
        if "notification" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_09_SettingsPage_Notificationp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_09_SettingsPage_Notificationf.png")

    def clickondropdownMasterBank(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownMasterBank_xpath).click()

    def clickonAddNewBank(self):
        self.driver.find_element(By.XPATH,self.btnAddNewBank_xpath).click()

    def setAddBank(self):
        type=Select(self.driver.find_element(By.XPATH,self.selectType_xpath))
        type.select_by_visible_text("Add Bank")
        self.driver.find_element(By.XPATH,self.txtPayeeNAme_xpath).send_keys("Vishal test")
        self.driver.find_element(By.XPATH,self.txtBankNAme_xpath).send_keys("STATE BANK OF INDIA")
        self.driver.find_element(By.XPATH,self.txtAccountType_xpath).send_keys("Current Account")
        self.driver.find_element(By.XPATH,self.txtAccountNumber_xpath).send_keys("989898989812")
        self.driver.find_element(By.XPATH,self.txtIFCcode_xpath).send_keys("SBIN0000555")
        self.driver.find_element(By.XPATH,self.txtBranchName_xpath).send_keys("Vasundhara Ghaziabad")
        self.driver.find_element(By.XPATH,self.btnSaveBank_xpath).click()
        if "bankmaster" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_09_SettingsPage_MasterBankp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_09_SettingsPage_MasterBankf.png")

    def clickondropdownServiceGateway(self):
        self.driver.find_element(By.XPATH,self.lnkdropdownGateways_xpath).click()

    def clickonAddServiceGateway(self):
        self.driver.find_element(By.XPATH,self.btnAddNewGateway_xpath).click()

    def setAddServiceGateway(self):
        service=Select(self.driver.find_element(By.XPATH,self.dropdownService_xpath))
        service.select_by_visible_text("PAYIN")
        vendor=Select(self.driver.find_element(By.XPATH,self.dropdownVendor_xpath))
        vendor.select_by_visible_text("runpaisa")
        self.driver.find_element(By.XPATH,self.txtGatewayLimit_xpath).send_keys("500000")
        self.driver.find_element(By.XPATH,self.txtGatewayCategory_xpath).send_keys("PG1")
        self.driver.find_element(By.XPATH,self.txtDomesticCardNetwork_xpath).send_keys("MasterCard")
        self.driver.find_element(By.XPATH,self.btnCreateGateway_xpath).click()
        if "service-gateways" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_09_SettingsPage_MasterBankp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_09_SettingsPage_MasterBankf.png")

    def clickonTeamsMenu(self):
        self.driver.find_element(By.XPATH,self.lnkTeamsMenu_xpath).click()

    