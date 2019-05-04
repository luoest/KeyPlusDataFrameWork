from testcases.TestLogin import testLogin
from performance.PagePerformance import getOpenLocalFile, getClose
from utilities.getFilePath import excel_path

if __name__ == '__main__':
    testLogin()
    getOpenLocalFile(excel_path)
    getClose()
