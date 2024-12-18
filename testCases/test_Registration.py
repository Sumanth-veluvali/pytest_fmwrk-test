import os.path
import time
from datetime import datetime

import pytest
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Account_register_page import AccountRegistrationPage
from pageObjects.HomePage import Homepage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.support import expected_conditions as EC



class Test_Account_Registraition:
    url = ReadConfig.getAppUrl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.order(1)
    def test_account_reg(self,setup):
        self.driver = setup
        self.driver.get(self.url)

        # self.element = self.driver.find_element(By.XPATH,'//*[@id="RlquG0"]/div/label/input)')
        # action = ActionChains(self.driver)
        # action.click_and_hold(self.element)
        # action.perform()
        # time.sleep(3)
        #
        # action.release(self.element)
        # action.perform()
        # time.sleep(3)

        self.logger.info("xxxOpened URLxxx")
        self.driver.maximize_window()

        self.logger.info("xxxTest Case startedxxx")
        self.hp = Homepage(self.driver)
        # self.element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(self.hp.clickregisterlink()))
        self.hp.clickregisterlink()

        self.logger.info("xxxRegistration Page openedxxx")
        self.arp = AccountRegistrationPage(self.driver)
        self.logger.info("xxxFilling Registration Pagexxx")
        self.arp.genderMale()
        self.arp.setFirstName('TestFname')
        self.arp.setLastName("testLname")
        self.arp.dateOfBirth("19", 'December', '1999')
        self.arp.setMail("tester2345678@gmail.com")
        self.arp.setCompanyName('testingcompany')
        self.arp.setPassword('test@123')
        self.arp.setConfirmPassword('test@123')
        self.arp.clickRegisterButton()
        self.logger.info("xxxClicked on Registration Buttonxxx")
        self.confirmation_msg = self.arp.getConfirmationmessage()

        if self.confirmation_msg == "Your registration completed":
            assert True
            self.logger.info("xxxTest Case Ended and Passedxxx")
            self.driver.close()
        else:
            self.driver.get_screenshot_as_file(os.path.abspath(os.curdir + "\\screenshots\\"+ datetime.now().strftime("%d-%m-%Y %H-%M-%S") +'reg.png'))
            self.logger.info("xxx Test Case Ended and Failedxxx")
            assert False





