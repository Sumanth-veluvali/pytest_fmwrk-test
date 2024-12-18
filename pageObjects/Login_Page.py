from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Login:
    #XPATHS of login Page:
    email = '//*[@id="Email"]'
    password = '//*[@id="Password"]'
    login_button = '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button'
    logout_link = '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'
    myaccount_link = "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a"
    myaccount_linkText  = "My account"


    def __init__(self,driver):
        self.driver = driver

    def setemail(self,email):
        self.driver.find_element(By.XPATH, self.email).send_keys(email)

    def setpassword(self,pwd):
        self.driver.find_element(By.XPATH, self.password).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    # def getloginconfirmation(self):
    #     try:
    #         self.driver.find_element(By.XPATH, self.logout_link).is_displayed()
    #     except:
    #         None
    def getloginconfirmation(self):
        self.my_account_occurence = self.driver.find_elements(By.LINK_TEXT, self.myaccount_linkText)
        return len(self.my_account_occurence)

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_link).click()




