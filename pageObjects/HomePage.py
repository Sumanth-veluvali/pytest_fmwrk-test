from selenium.webdriver.common.by import By
from selenium import webdriver


class Homepage:
    #Homepage xpaths:
    register_link = "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a"
    login = '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'

    def __init__(self,driver):
        self.driver = driver

    def clickregisterlink(self):
        self.driver.find_element(By.XPATH,self.register_link).click()

    def clickLoginlink(self):
        self.driver.find_element(By.XPATH,self.login).click()
