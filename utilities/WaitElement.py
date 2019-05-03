# encoding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WaitPageElement(object):
    def __init__(self, driver):
        self.driver = driver
        self.locTypeDict={'id': By.ID,
                          'name': By.NAME,
                          'link text': By.LINK_TEXT,
                          'partial link text': By.PARTIAL_LINK_TEXT,
                          'xpath': By.XPATH,
                          'css': By.CSS_SELECTOR}
        self.wait = WebDriverWait(self.driver, 10)

    def getPresentElement(self, locType, loc):
        """
        显式等待出现在DOM中，但不一定可见的元素。若存在，返回该页面元素对象。
        """
        print(locType.lower())
        print(self.locTypeDict[locType.lower()])
        try:
            if locType.lower() in self.locTypeDict:
                element = self.wait.until(EC.presence_of_element_located((self.locTypeDict[locType.lower()], loc)))
                return element
            else:
                raise  TypeError('未找到匹配的定位方式。')
        except Exception as e:
            raise e

    def getVisibleElement(self, locType, loc):
        """
        显式等待出现在DOM中并且可见的元素，返回该元素对象。
        """
        print(locType.lower())
        print(self.locTypeDict[locType.lower()])
        try:
            if locType.lower() in self.locTypeDict:
                element = self.wait.until(EC.visibility_of_element_located((self.locTypeDict[locType.lower()], loc)))
                return element
            else:
                raise  TypeError('未找到匹配的定位方式。')
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    try:
        driver.get("http://localhost")
        wait = WaitPageElement(driver)
        wait.getPresentElement('xpath', '//input[@name="username"]').send_keys("gotIt")
        wait.getPresentElement('css', 'input[name="password"]').send_keys("gotIt123")
        wait.getVisibleElement('name', 'Submit').click()
        wait.getVisibleElement('partial link text', '请点击这里').click()
    finally:
        driver.quit()

