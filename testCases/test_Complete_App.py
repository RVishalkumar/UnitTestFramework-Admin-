import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from PageObjects.DashboardPage import DashboardPage
from PageObjects.LoginPage import LoginPage
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
        #driver.implicitly_wait(5)

    def test_01_loginPages(self):
        self.lp = LoginPage(driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickonView()
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
        self.dp.clickonNotification()
        self.dp.clickonProfileImage()
        self.dp.clickonProfileTag()
        self.dp.clickonProfileImage()
        self.dp.clickonChangePassword()


    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Passed")
        driver.close()

if __name__ == "__main__":
    unittest.main()
