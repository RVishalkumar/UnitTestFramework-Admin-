from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.wait import Wait


class LoginPage:


    textbox_username_name = "email"
    textbox_password_name = "password"
    btnLogin_xpath = "(//button[@type='submit'])[1]"
    textOTP1_xpath = "//input[@id='otc-1']"
    textOTP2_xpath = "//input[@id='otc-2']"
    textOTP3_xpath = "//input[@id='otc-3']"
    textOTP4_xpath = "//input[@id='otc-4']"
    textOTP5_xpath = "//input[@id='otc-5']"
    textOTP6_xpath = "//input[@id='otc-6']"
    btnContinue_xpath = "//button[text()='Continue']"
    btmAlert_xpath = "//button[@onclick='sfmX()']"




    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)

    def clickonView(self):
        Wait.wait_for_click(self.driver,(By.XPATH,"//*[@id='loginForm']/div[2]/span")).click()
        if "login" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_01_LoginPage_loginpass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_01_LoginPage_loginfail.png")

    def clickLogin(self):
        Wait.wait_for_click(self.driver,(By.XPATH, self.btnLogin_xpath)).click()




        #self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",login_btn)

        #self.driver.execute_script("arguments[0].click();",login_btn)

    def setOTP1(self, otp):
        Wait.wait_for_visible(self.driver,(By.XPATH, self.textOTP1_xpath)).send_keys(otp)

    def setOTP2(self, otp):
        self.driver.find_element(By.XPATH, self.textOTP2_xpath).send_keys(otp)

    def setOTP3(self, otp):
        self.driver.find_element(By.XPATH, self.textOTP3_xpath).send_keys(otp)

    def setOTP4(self, otp):
        self.driver.find_element(By.XPATH, self.textOTP4_xpath).send_keys(otp)

    def setOTP5(self, otp):
        self.driver.find_element(By.XPATH, self.textOTP5_xpath).send_keys(otp)

    def setOTP6(self, otp):
        self.driver.find_element(By.XPATH, self.textOTP6_xpath).send_keys(otp)
        if "verify-otp" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_01_LoginPage_VerifyOTP.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_01_LoginPage_VerifyOTP.png")

    # def setOTP(self, otp1, otp2, otp3, otp4, otp5, otp6):
    #     self.driver.find_element(By.XPATH,self.textOTP1_xpath).send_keys()
    #     self.driver.find_element(By.XPATH,self.textOTP2_xpath).send_keys()
    #     self.driver.find_element(By.XPATH,self.textOTP3_xpath).send_keys()
    #     self.driver.find_element(By.XPATH,self.textOTP4_xpath).send_keys()
    #     self.driver.find_element(By.XPATH,self.textOTP5_xpath).send_keys()
    #     self.driver.find_element(By.XPATH,self.textOTP6_xpath).send_keys()


    def clickonContinue(self):
        self.driver.find_element(By.XPATH,self.btnContinue_xpath).click()

    def clickonPopUp(self):
        # action = ActionChains(self.driver)
        # action.send_keys(Keys.ENTER).perform()
        self.driver.find_element(By.XPATH,self.btmAlert_xpath).click()