from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DashboardPage:

    btnWallet_xpath = "//div[@class='navbar-header']/div/div[2]/div/div[1]"
    btnMode_xpath = "//button[@title='Switch to Light/Dark mode']"
    btnNotification_xpath = "//button[@title='Check Your Alerts']"
    btnProfileImage_xpath = "//div[@class='col-auto']/div/div[3]"
    tagProfile_xpath = "//a[@href='https://b2b.digifintel.com/my/profile']"
    tagChangePassword_xpath = "//a[@href='https://b2b.digifintel.com/change/password']"
    txtOldPassword_xpath = "//input[@id='old_password']"
    txtNewPassword_xpath = "//input[@id='new_password']"
    txtConfirmPassword_xpath = "//input[@id='new_password_confirmation']"
    btnSubmit_xpath = "//div[@class='mt-10 d-flex align-items-center justify-content-center gap-3']/button"

    def __init__(self,driver):
        self.driver = driver

    def clickonWallet(self):
        self.driver.find_element(By.XPATH,self.btnWallet_xpath).click()

    def clickonMode(self):
        action = ActionChains(self.driver)
        doubleclick=self.driver.find_element(By.XPATH,self.btnMode_xpath)
        action.double_click(doubleclick).perform()

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
        self.driver.find_element(By.XPATH,self.txtNewPassword_xpath).send_keys("Test@@123")
        self.driver.find_element(By.XPATH,self.txtConfirmPassword_xpath).send_keys("Test@@123")
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()


