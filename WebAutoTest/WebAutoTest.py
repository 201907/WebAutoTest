import pandas as pd
import numpy as np
import io,sys,configparser,os
from selenium import webdriver
from time import sleep

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
        data = pd.read_excel(configFolder + "/" + configFile,sheet_name = "action",header = 0)
        url = data.iloc[0,1]
        driver.get(url)
        action = data.iloc[2:,:]
        for row in action.fillna(0).iterrows():
            element = driver.find_element_by_css_selector(row[1].CSS)
            action = row[1].action
            time = row[1].time
            input = row[1].input
            time = row[1].time
            if action == "输入内容":
                element.clear()
                element.send_keys(input)
            elif action == "点击":
                element.click()
            elif action == "切换窗口":
                driver.switch_to_window(input)

            sleep(time)

if __name__ == "__main__":
        init()
        execute()