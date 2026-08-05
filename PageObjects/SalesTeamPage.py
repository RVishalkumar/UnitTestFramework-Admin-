from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SalesTeamPage:

    btnAddNewUser_xpath = "//a[@href='https://b2b.digifintel.com/salesteam/create']"
    dropdownAssignRole = "//select[@id='role']"
    txtFristName_xpath = "//input[@id='fname']"
    txtLastName_name = "lname"
    txtEmail_name = "email"
    txtMobileNumber_xpath = "//input[@id='mobile']"
    txtPassword_xpath = "//input[@id='password_confirmation']"
    txtDOB_name = "dateofbirth"
    txtFatherName_name = "fathername"
    txtMotherName_name = "mothername"
    txtAadharNumber_name = "aadharnumber"
    txtPanCard_name = "pancardnumber"
    txtPinCode_xpath = "//input[@id='pincode']"
    dropdownState_xpath = "//select[@id='state']"
    dropdownCity_xpath = "//select[@id='city']"
    textareaAddress_xpath = "//textarea[@name='address']"
    chooseProfileImage_name = "profileimg"
    chooseAadharFImage_name = "adfrontimg"
    chooseAadharBImage_xpath = "//form[@id='userForm']/div/div[20]/input"
    choosePanCard_xpath = "//form[@id='userForm']/div/div[21]/input"
    btnSave_xpath = "//form[@id='userForm']/div[2]/button"
    lnkServicePanelMenu_xpath = "//*[@id='sidebar-menu']/li[11]"




    def __init__(self,driver):
        self.driver = driver

    def clickonAddNewUser(self):
        self.driver.find_element(By.XPATH,self.btnAddNewUser_xpath).click()

    def setAddTeam(self):
        role=Select(self.driver.find_element(By.XPATH,self.dropdownAssignRole))
        role.select_by_visible_text("zonal head")
        self.driver.find_element(By.XPATH,self.txtFristName_xpath).send_keys("New Zonal")
        self.driver.find_element(By.NAME,self.txtLastName_name).send_keys("Head")
        self.driver.find_element(By.NAME.self.txtEmail_name).send_keys("zonalhead@gmail.com")
        self.driver.find_element(By.XPATH,self.txtMobileNumber_xpath).send_keys("9897969594")
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys("Test@@123")
        self.driver.find_element(By.NAME,self.txtDOB_name).send_keys("01-01-1996")
        self.driver.find_element(By.NAME,self.txtFatherName_name).send_keys("c.b.singh")
        self.driver.find_element(By.NAME,self.txtMotherName_name).send_keys("p singh")
        self.driver.find_element(By.NAME,self.txtAadharNumber_name).send_keys("456723458965")
        self.driver.find_element(By.NAME,self.txtPanCard_name).send_keys("BLFPK739h")
        self.driver.find_element(By.XPATH,self.txtPinCode_xpath).send_keys("201019")
        state=Select(self.driver.find_element(By.XPATH,self.dropdownState_xpath))
        state.select_by_visible_text("Uttar Pradesh")
        city=Select(self.driver.find_element(By.XPATH,self.dropdownCity_xpath))
        city.select_by_visible_text("Ghaziabad")
        self.driver.find_element(By.XPATH,self.textareaAddress_xpath).send_keys("F808/807 Vaishali")
        self.driver.find_element(By.NAME,self.chooseProfileImage_name).send_keys("C://Users//dell//Pictures//Screenshots//Screenshot 2026-07-06 013116.png")
        self.driver.find_element(By.NAME,self.chooseAadharFImage_name).send_keys("C://Users//dell//Pictures//Screenshots//Screenshot 2026-07-06 013159.png")
        self.driver.find_element(By.XPATH,self.chooseAadharBImage_xpath).send_keys("C:/Users//dell//Pictures//Screenshots//Screenshot 2026-07-06 014159.png")
        self.driver.find_element(By.XPATH,self.choosePanCard_xpath).send_keys("C://Users//dell//Pictures//Screenshots//Screenshot 2026-07-02 153735.png")
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
        if "salesteam" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_11_SalesTeamsPage_ADDTeamp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_11_SalesTeamsPage_ADDTeamsf.png")

    def clickonServicePanelMenu(self):
        self.driver.find_element(By.XPATH,self.lnkServicePanelMenu_xpath).click()


