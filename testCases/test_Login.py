import os
import pytest

from datetime import datetime
from pageObjects.HomePage import Homepage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.Login_Page import Login

class Test_Login:
    url = ReadConfig.getAppUrl()
    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.order(2)
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)

        self.logger.info("xxx Opened URL xxx")
        self.driver.maximize_window()

        self.logger.info("xxx Test Case started xxx")
        self.hp = Homepage(self.driver)
        self.hp.clickLoginlink()

        self.logger.info("xxx Login page opened xxx")
        self.lg = Login(self.driver)
        self.lg.setemail('tester2345678@gmail.com')
        self.lg.setpassword('test@123')

        self.logger.info("xxx Entered Credentials xxx")

        self.lg.clickLogin()
        self.loginconfirmation = self.lg.getloginconfirmation()

        if self.loginconfirmation > 1:
            self.logger.info("xxx Test case ended and Logged into application xxx")
            self.driver.close()
            assert True

        else:
            self.logger.info("xxx Test cases ended and Login failed xxx")
            self.driver.get_screenshot_as_file(os.path.abspath(os.curdir + "\\screenshots\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + 'Login.png'))
            self.driver.close()
            assert False



