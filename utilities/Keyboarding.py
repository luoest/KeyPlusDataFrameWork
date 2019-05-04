import win32api
import win32con

class Keyboarding():

    key_dict = {'ctrl': 0x11,
                'a': 0x41,
                'c': 0x43,
                'v': 0x56,
                'x': 0x58,
                'enter': 0x0D}

    @staticmethod
    def keyDown(keyName):
        win32api.keybd_event(Keyboarding.key_dict[keyName], 0)

    @staticmethod
    def keyUp(keyName):
        win32api.keybd_event(Keyboarding.key_dict[keyName], 0, win32con.KEYEVENTF_KEYUP)

    @staticmethod
    def twoKeys(key1, key2):
        Keyboarding.keyDown(key1)
        Keyboarding.keyDown(key2)
        Keyboarding.keyUp(key2)
        Keyboarding.keyUp(key1)

    @staticmethod
    def oneKey(keyName):
        Keyboarding.keyDown(keyName)
        Keyboarding.keyUp(keyName)


if __name__ == '__main__':
    from performance.PagePerformance import *
    getBrowser('firefox')
    getUrl("https://www.baidu.com")
    getSendKeys('id', 'kw', 2019)
    getSleep(1)

    Keyboarding.twoKeys('ctrl', 'a')
    getSleep(1)
    Keyboarding.twoKeys('ctrl', 'x')
    getSleep(1)
    Keyboarding.twoKeys('ctrl', 'v')
    getSleep(1)
    Keyboarding.twoKeys('ctrl', 'c')
    getSleep(1)
    Keyboarding.twoKeys('ctrl', 'v')
    getSleep(1)
    Keyboarding.twoKeys('ctrl', 'v')
    getSleep(1)
    Keyboarding.twoKeys('ctrl', 'v')
    getSleep(1)
    Keyboarding.twoKeys('ctrl', 'v')
    getSleep(1)
    Keyboarding.oneKey('enter')
    getSleep(1)
    getClose()




