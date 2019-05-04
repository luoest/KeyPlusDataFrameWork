import win32clipboard as w
import win32con

class Clipboarding():

    @staticmethod
    def setText(contentStr):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, str(contentStr))
        w.CloseClipboard()

    @staticmethod
    def getText():
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()
        return d


if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Firefox()
    driver.get('https://www.baidu.com')
    Clipboarding.setText(2019)
    Clipboarding.getText()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

