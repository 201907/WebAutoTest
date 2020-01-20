import pandas as pd
import io,sys,configparser,os
from selenium import webdriver

config = configparser.ConfigParser()
configFileLst = []
url = ""
configFolder = ""
def init():
    global config
    global url
    global driver
    global configFileLst
    global configFolder
    config.read("mypy.ini")
    url = config.get("env","url")
    browser = config.get("env","browser")
    if browser == "0":
        driver = webdriver.Ie()
    elif browser == "1":
        driver = webdriver.Chrome()
    elif browser == "2":
        driver = webdriver.Firefox()
    elif browser == "3":
        driver = webdriver.Opera()
    else:
        print("qi")
        sys.exit(0)
    configFolder = config.get("env","actionFolder")
    configFileLst = os.listdir(configFolder)

def execute():
    global configFolder
    for configFile in configFileLst:
        data = pd.read_excel(configFolder + "/" + configFile,sheet_name = "action")
        print(data)

if __name__ == "__main__":
    init()
    execute()