import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + "\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getAppUrl():
        url = config.get('commonInfo','base_url')
        return url

    @staticmethod
    def getusername():
        username = config.get('commonInfo','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('commonInfo', 'password')
        return password

