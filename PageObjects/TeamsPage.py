from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class TeamsPage:

    btnAddNewTeams_xpath = "//div[@class='dashboard-main-body']/div[2]/div/div/div[1]/a"
    txtFirstNAme_name = "fname"
    txtLastName_name = "lname"
    txtEmail_name = "email"
    txtMobile_name = "mobile"
    txtPrefix_name = "prefix"
    txtPassword_name = "password"
    txtDateOfBirth_name = "dateofbirth"
    dropdownAssineRole_name = "role"
    txtFatherName_name = "fathername"
    txtMothername_name = "mothername"
    txtAadhar_name = "aadharnumber"
    txtPanCard_name = "pancardnumber"
    txtPinCode_name = "pincode"
    txtCountry_name = "country"
    dropdownState_xpath = "//select[@name='state']"
    dropdownCity_xpath = "//select[@name='city']"
    txtDistrict_name = "//input[@name='district']"
    textareaAddress_xpath = "//textarea[@name='address']"
    chooseProfileImage_name = "profileimg"
    btnSave_xpath = "//div[@class='card-body p-0']/form/div[2]/button"
    btnActive_xpath = "//input[@id='status1']"
    btnDashBoardTitle_xpath = "//div[@id='permissionsAccordion']/div[9]/h2/div/input"
    btnUpdatePermissions_xpath = "//div[@class='card-body p-24']/form/div[3]/button"
    lnkSalesTeamMenu_xpath = "//*[@id='sidebar-menu']/li[10]"




    def __init__(self,driver):
        self.driver = driver

    def clickonAddNewTeams(self):
        self.driver.find_element(By.XPATH,self.btnAddNewTeams_xpath).click()

    def setAddTeam(self):
        self.driver.find_element(By.NAME,self.txtFirstNAme_name).send_keys("Vishal")
        self.driver.find_element(By.NAME,self.txtLastName_name).send_keys("Singh")
        self.driver.find_element(By.NAME,self.txtEmail_name).send_keys("mail.vickyvishal@gmail.com")
        self.driver.find_element(By.NAME,self.txtMobile_name).send_keys("9407271094")
        self.driver.find_element(By.NAME,self.txtPrefix_name).send_keys("Mr")
        self.driver.find_element(By.NAME,self.txtPassword_name).send_keys("Test@@123")
        self.driver.find_element(By.XPATH,self.txtDateOfBirth_name).send_keys("14/10/1998")
        role=Select(self.driver.find_element(By.NAME,self.dropdownAssineRole_name))
        role.select_by_visible_text("onboard team")
        self.driver.find_element(By.NAME,self.txtFatherName_name).send_keys("Father")
        self.driver.find_element(By.NAME,self.txtMothername_name).send_keys("Mother")
        self.driver.find_element(By.NAME,self.txtAadhar_name).send_keys("471221013233")
        self.driver.find_element(By.NAME,self.txtPanCard_name).send_keys("BLFPK0736H")
        self.driver.find_element(By.NAME,self.txtPinCode_name).send_keys("841301")
        self.driver.find_element(By.NAME,self.txtCountry_name).send_keys("India")
        state=Select(self.driver.find_element(By.XPATH,self.dropdownState_xpath))
        state.select_by_visible_text("Bihar")
        city=Select(self.driver.find_element(By.XPATH,self.dropdownCity_xpath))
        city.select_by_visible_text("Chapra")
        self.driver.find_element(By.XPATH,self.txtDistrict_name).send_keys("Saran")
        self.driver.find_element(By.XPATH,self.textareaAddress_xpath).send_keys("p n nagar")
        self.driver.find_element(By.XPATH,self.chooseProfileImage_name).send_keys("C://Users//dell//Pictures//Screenshots//pic.png")
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

    def setManageTeams(self):
        rows = self.driver.find_element(By.XPATH, "//table[@id='tableData']/tbody/tr")
        for row in rows:
            email = row.find_element(By.XPATH, "./td[4]").text.strip()
            if email == "mail.vickyvishal@gmail.com":
                row.find_element(By.XPATH, "./td[8]//a[@class='allow_services_edit']").click()
                break
        self.driver.find_element(By.XPATH,self.btnActive_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

    def setAllowPermissions(self):
        rows = self.driver.find_element(By.XPATH, "//table[@id='tableData']/tbody/tr")
        for row in rows:
            email = row.find_element(By.XPATH, "./td[4]").text.strip()
            if email == "mail.vickyvishal@gmail.com":
                row.find_element(By.XPATH, "./td[8]//a[@class='dropdown-item allow_services_btn']").click()
                break
        self.driver.find_element(By.XPATH,self.btnDashBoardTitle_xpath).click()
        self.driver.find_element(By.XPATH,self.btnUpdatePermissions_xpath).click()

    def clickonSalesTeamsMenu(self):
        self.driver.find_element(By.XPATH,self.lnkSalesTeamMenu_xpath).click()








