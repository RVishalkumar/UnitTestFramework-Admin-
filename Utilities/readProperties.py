import configparser
config = configparser.RawConfigParser()

config.read("C://Users//dell//PycharmProjects//UnitTestFrameWork(admin)//Configuration//config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('uat info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('uat info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('uat info', 'password')
        return password

    @staticmethod
    def getOTP():
        otp = config.get('uat info','otp')
        return otp
