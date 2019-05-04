from utilities.ObjectMapping import getWaitElement
from utilities.WaitElement import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utilities.ObjectMapping import getWaitElement
from utilities.Keyboarding import Keyboarding
from utilities.Clipboarding import Clipboarding
import time
import os

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

def getUrl(url):
    driver.get(url)

def getElement(locType, loc):
    getWaitElement(driver, locType, loc)

def getClear(locType, loc):
    getWaitElement(driver, locType, loc).clear()

def getSendKeys(locType, loc, value):
    getWaitElement(driver, locType, loc).send_keys(value)

def getClick(locType, loc):
    getWaitElement(driver, locType, loc).click()

def getPageSource():
    return driver.page_source

def getAssertIn(element):
    try:
        assert element in getPageSource(), '页面代码中没有发现目标元素：%s'%str(element)
    except Exception as e:
        print(e)
        raise e

def getTitle():
    title = driver.title
    msg = '当前页面的标题是：' + str(title)
    print(msg)
    return title

def getCurrent_url():
    current_url = driver.current_url
    msg = '当前页面的地址是：' + str(current_url)
    print(msg)
    return current_url

def getSleep(sleeeSec):
    time.sleep(sleeeSec)

def getClose():
    driver.quit()

def getOpenLocalFile(file):
    os.startfile(file)

def getUploadLocalFile(locType, loc, file):
    if browser_name == 'chrome':
        Clipboarding.setText(file)
        Clipboarding.getText()
        getClick(locType, loc)
        getSleep(2)
        Keyboarding.twoKeys('ctrl', 'v')
        getSleep(1)
        Keyboarding.oneKey('enter')
    else:
        getSendKeys(locType, loc, file)



if __name__ == '__main__':
    getBrowser('chrome')
    getUrl('http://localhost')
    getSendKeys('name', 'username', 'gotIt')
    getSendKeys('name', 'password', 'gotIt123')
    getClick('name', 'Submit')
    getTitle()
    getCurrent_url()
    getClick('partial link text', '请点击这里')
    getAssertIn('我的空间')
    getAssertIn('火星人的地盘')
    getSleep(1)
    getClose()
