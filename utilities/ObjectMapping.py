# encoding=utf-8
from selenium.webdriver.support.wait import WebDriverWait

def getWaitElement(driver, locType, locator):
    """
    Call the method to get page element in a limited time.

    :param driver: Instance of WebDriver (Ie, Firefox, Chrome or Remote)
    :param locType: page element locator type(Ie, id, xpath, link_text, etc)
    :param locator: page element locator
    :return: page element
    """
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(lambda driver: driver.find_element(locType, locator))
        getHighlightElement(driver, element)
        return element
    except Exception as e:
        raise e

def getHighlightElement(driver, element):
    """

    :param driver:
    :param element:
    :return:
    """
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                          element, "background: yellow; border: 2px solid red;")


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    getWaitElement(driver, 'id', 'kw').send_keys('天气预报')
    getWaitElement(driver, 'id', 'su').click()
