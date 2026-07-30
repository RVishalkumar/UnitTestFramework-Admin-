from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CommissionsPage:

    btnNewCommission_xpath = "//a[@href='https://b2b.digifintel.com/aeps/commission/create?service=aeps']"
    txtPackagetitle_xpath = "//input[@id='title']"
    dropdownPackageType_xpath = "//select[@id='pkgtype']"
    txtFromAmount_xpath = "//input[@id='fromamount']"
    txtToAmount_xpath = "//input[@id='toamount']"
    txtWhitelabelComm_xpath = "//input[@id='whitelabel']"
    txtMasterDistributorComm_xpath = "//input[@id='mdistributer']"
    txtDistributor_xpath = "//input[@id='distributer']"
    txtRetailerComm_xpath = "//input[@id='retailer']"
    txtCalculation_xpath = "//input[@id='calculation']"
    btnStatus_xpath = "//input[@id='status1']"


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
        self.driver.find_element(By.XPATH,self.txtDistributor_xpath).send_keys("0.33")
        self.driver.find_element(By.XPATH,self.txtRetailerComm_xpath).send_keys("0.1")
        self.driver.find_element(By.XPATH,self.txtCalculation_xpath).send_keys("")
        self.driver.find_element(By.XPATH,self.btnStatus_xpath).click()
        self.driver.find_element(By.XPATH,self.)
