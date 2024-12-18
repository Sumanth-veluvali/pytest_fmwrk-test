from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AccountRegistrationPage:
    #Registration page XPATHS:
    register_link = "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a"
    gender_male = '//*[@id="gender-male"]'
    gender_female = '// *[@id="gender-female"]'
    first_name = '//*[@id="FirstName"]'
    last_name = '//*[@id="LastName"]'
    day = '//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]'
    month = '//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]'
    year = '//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]'
    mail = '//*[@id="Email"]'
    company_name = '//*[@id="Company"]'
    password = '//*[@id="Password"]'
    conf_password = '//*[@id="ConfirmPassword"]'
    reg_button = '//*[@id="register-button"]'
    conf_msg = '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]'


    def __init__(self,driver):
        self.driver = driver

    def genderMale(self):
        self.driver.find_element(By.XPATH, self.gender_male).click()
    def genderFemale(self):
        self.driver.find_element(By.XPATH, self.gender_female).click()
    def setFirstName(self,Fname):
        self.driver.find_element(By.XPATH, self.first_name).send_keys(Fname)
    def setLastName(self,Lname):
        self.driver.find_element(By.XPATH, self.last_name).send_keys(Lname)

    def dateOfBirth(self,Day,Month,Year):
        dob_day = Select(self.driver.find_element(By.XPATH, self.day))
        dob_day.select_by_visible_text(Day)
        dob_month = Select(self.driver.find_element(By.XPATH, self.month))
        dob_month.select_by_visible_text(Month)
        dob_year = Select(self.driver.find_element(By.XPATH, self.year))
        dob_year.select_by_visible_text(Year)

    def setMail(self,Mail):
        self.driver.find_element(By.XPATH, self.mail).send_keys(Mail)

    def setCompanyName(self,cmpny_name):
        self.driver.find_element(By.XPATH, self.company_name).send_keys(cmpny_name)

    def setPassword(self,Pwd):
        self.driver.find_element(By.XPATH, self.password).send_keys(Pwd)

    def setConfirmPassword(self,Pwd):
        self.driver.find_element(By.XPATH, self.conf_password).send_keys(Pwd)

    def clickRegisterButton(self):
        self.driver.find_element(By.XPATH, self.reg_button).click()

    def getConfirmationmessage(self):
        try:
            return self.driver.find_element(By.XPATH, self.conf_msg).text
        except:
            None




















