from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Utilities.wait import Wait


class DashboardPage:

    btnWallet_xpath = "//div[@class='navbar-header']/div/div[2]/div/div[1]"
    btnMode_xpath = "//button[@title='Switch to Light/Dark mode']"
    btnNotification_xpath = "//button[@title='Check Your Alerts']"
    btnProfileImage_xpath = "//div[@class='col-auto']/div/div[3]"
    tagProfile_xpath = "//a[@href='https://b2b.digifintel.com/my/profile']"
    tagChangePassword_xpath = "//a[@href='https://b2b.digifintel.com/change/password']"
    txtOldPassword_xpath = "//input[@id='old_password']"
    btnView1_xpath = "//span[@data-toggle='#old_password']"
    txtNewPassword_xpath = "//input[@id='new_password']"
    btnView2_xpath = "//span[@data-toggle='#new_password']"
    txtConfirmPassword_xpath = "//input[@id='new_password_confirmation']"
    btnView3_xpath = "//span[@data-toggle='#new_password_confirmation']"
    btnSubmit_xpath = "//div[@class='mt-10 d-flex align-items-center justify-content-center gap-3']/button"
    tagSettings_xpath = "//a[@href='https://b2b.digifintel.com/mysetting/all']"
    btnTransaction_xpath = "//button[@id='pills-change-tpin-tab']"
    txtTransactionPin_xpath = "//input[@id='txnpin']"
    txtLoginPassword_xpath = "//input[@id='acpassword']"
    btnSave_xpath = "//div[@id='pills-change-tpin']/form/div[3]/button"
    tagLogout_xpath = "//a[@onclick='handleLogout()']"
    lnkAccountMenu_xpath = "//*[@id='sidebar-menu']/li[2]"
    lnkdropdownManageUser_xpath = "//*[@href='https://b2b.digifintel.com/users']"



    def __init__(self,driver):
        self.driver = driver

    def clickonWallet(self):
        self.driver.find_element(By.XPATH,self.btnWallet_xpath).click()

    def clickonMode(self):
        # action = ActionChains(self.driver)
        # doubleclick=self.driver.find_element(By.XPATH,self.btnMode_xpath)
        # action.double_click(doubleclick).perform()
        self.driver.find_element(By.XPATH, self.btnMode_xpath).click()

    def clickonNotification(self):
        self.driver.find_element(By.XPATH,self.btnNotification_xpath).click()

    def clickonProfileImage(self):
        self.driver.find_element(By.XPATH,self.btnProfileImage_xpath).click()

    def clickonProfileTag(self):
        self.driver.find_element(By.XPATH,self.tagProfile_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "profile" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_02_DashboardPage_ProfileTagp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_02_DashboardPage_ProfileTagf.png")

    def clickonChangePassword(self):
        self.driver.find_element(By.XPATH,self.tagChangePassword_xpath).click()
        self.driver.find_element(By.XPATH,self.txtOldPassword_xpath).send_keys("Test@@123")
        self.driver.find_element(By.XPATH,self.btnView1_xpath).click()
        self.driver.find_element(By.XPATH,self.txtNewPassword_xpath).send_keys("Test@@123")
        self.driver.find_element(By.XPATH,self.btnView2_xpath).click()
        self.driver.find_element(By.XPATH,self.txtConfirmPassword_xpath).send_keys("Test@@123")
        self.driver.find_element(By.XPATH,self.btnView3_xpath).click()
        if "password" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_02_DashboardPage_PasswordTagp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_02_DashboardPage_PasswordTagf.png")
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()

    def clickonSettings(self):
        self.driver.find_element(By.XPATH,self.tagSettings_xpath).click()
        if "all" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_02_DashboardPage_SettingsTagp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_02_DashboardPage_SettingsTagf.png")
        self.driver.find_element(By.XPATH,self.btnTransaction_xpath).click()
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.txtLoginPassword_xpath).send_keys("Test@@123")
        if "all" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_02_DashboardPage_TransactionPinp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_02_DashboardPage_TransactionPinf.png")
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

    def clickonLogout(self):
        self.driver.find_element(By.XPATH,self.tagLogout_xpath).click()

    def clickonAccountsMenu(self):
        dropdown = self.driver.find_element(By.XPATH,self.lnkAccountMenu_xpath)
        dropdown.click()
        Wait.wait_for_click(self.driver,(By.XPATH,self.lnkdropdownManageUser_xpath)).click()