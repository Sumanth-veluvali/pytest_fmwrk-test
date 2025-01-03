import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        # os.path.abspath(os.curdir) + "\\configurations\\config.ini")
        path = os.path.abspath(os.curdir + '\\logs\\automation.log')
        logging.basicConfig(filename=path, format= '%(asctime)s - %(levelname)s - %(message)s',
                            datefmt = '%m/%d/%Y %I:%M:%S%P') #%m/%d/%Y %I:%M:%S%P
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger