from utilities.ObjectMapping import getWaitElement
from utilities.WaitElement import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def getBrowser(browserName):
    global driver, browser_name, wait
    if browserName.lower() == 'chrome':
        chrome_option = Options()
        chrome_option.add_argument('--start-maximized')
        chrome_option.add_argument('--disable-extensions')
        driver = webdriver.Chrome(options = chrome_option)
    elif browserName.lower() == 'ie':
        caps = DesiredCapabilities.INTERNETEXPLORER
        caps['ignoreProtectedModeSettings'] = True
        driver = webdriver.Ie(capabilities = caps)
    else:
        driver = webdriver.Firefox()
    wait = WaitPageElement(driver)
    browser_name = browserName.lower()
