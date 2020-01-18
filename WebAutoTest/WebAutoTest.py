import pandas as pd
import io,sys,configparser
from selenium import webdriver

config = configparser.ConfigParser()
url = ""

def init():
    global config
    global url
    global driver
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
        print("没有找到对应的浏览器")
        sys.exit(0)

if __name__ == "__main__":
    init()