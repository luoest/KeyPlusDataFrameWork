from utilities.getFilePath import excel_path
from utilities.ExcelParsing import Exceling
from performance.PagePerformance import *

excelObj = Exceling()
excelObj.getWorkbook(excel_path)

case_sheetObj = excelObj.getSheet('用例')
case_choiceNo = 6
case_frameTypeNo = 2
case_resultNo = 8
case_timeNo = 7

key_methodNo = 2
key_resultNo = 7
key_timeNo = 8
key_picNo = 9

change_data_choiceNo = 12
change_key_methodNo = 1

def writeResult(sheet, content, rowNo, colNo, nowTime=None, timeNo=None, picPath=None, picNo=None, style=None):
    excelObj.getWriteByRowAndCol(sheet, content, rowNo, colNo, style)
    excelObj.getWriteTime(sheet, nowTime=nowTime, rowNo=rowNo, colNo=timeNo, style=style)
    if picPath:
        excelObj.getWriteByRowAndCol(sheet, content=picPath, rowNo=rowNo, colNo=picNo, style=style)
