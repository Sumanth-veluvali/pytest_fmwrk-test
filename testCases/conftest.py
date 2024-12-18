import os
from datetime import datetime
import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    # to open in normal window:
    driver = webdriver.Edge()
    return driver
    
    #to open in inprivate window:
    # edge_options = webdriver.EdgeOptions()
    # edge_options.add_argument("Inprivate")
    # edge_options.add_argument('headless')
    # driver = webdriver.Edge(edge_options)
    # return driver

#HTML Report Generation:
@pytest.mark.optionalhook
def pytest_configure(config):
    config._metadata["AppName"] = "Nop commerce"
    config._metadata["Tester"] = "Sumanth"

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)


@pytest.hookimpl(tryfirst = True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"




