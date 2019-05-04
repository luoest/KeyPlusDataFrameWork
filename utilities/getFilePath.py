import os
from performance.PagePerformance import getOpenLocalFile

base_path = os.path.dirname(os.path.dirname(__file__))

excel_path = base_path + '/testdata/localhost登录.xlsx'

loggerFile = base_path + '/config/loggering.conf'
# getOpenLocalFile(loggerFile)