from testcases.WriteTestResult import *
from utilities.KeyAndDataLog import *
import traceback

def changeInfo(key_sheet_obj, data_obj, rowNo):

    target_member = 0
    successful_member = 0

    choices = excelObj.getValueByCol(data_obj, change_data_choiceNo)
    for idc, choice in enumerate(choices[1:]):
        if choice.value == 'y':

            target_member += 1

            key_stepRowNo = excelObj.getRowAndColNum(key_sheet_obj)[0]

            stepNo = 0

            for step in range(2, key_stepRowNo + 1):
                method = excelObj.getValueByRow(key_sheet_obj, step)[change_key_methodNo].value
                locType = excelObj.getValueByRow(key_sheet_obj, step)[change_key_methodNo+1].value
                loc = excelObj.getValueByRow(key_sheet_obj, step)[change_key_methodNo+2].value
                cellName = excelObj.getValueByRow(key_sheet_obj, step)[change_key_methodNo+3].value

                if cellName:
                    cellName += str(idc + 2)
                    cellValue = excelObj.getCellValue(data_obj, cellName)

                    executing_method = method + '("%s", "%s", "%s")'%(locType, loc, cellValue)
                else:
                    executing_method = method + '("%s", "%s")' % (locType, loc)

                try:
                    eval(executing_method)
                    msg = '<通过>%s'%executing_method
                    print(msg)
                    logging.info(msg)
                    stepNo += 1
                except Exception as e:
                    print(e)
                    msg = '<未通过>%s' % executing_method
                    msg += str(e)
                    errorInfo = traceback.format_exc()
                    msg += str(errorInfo)
                    print(msg)
                    logging.debug(msg)

            if stepNo == key_stepRowNo - 1:
                msg = '<成功>%s: 共有步骤：%d, 执行成功步骤：%d'%(data_obj.title, key_stepRowNo-1, stepNo)
                print(msg)
                logging.info(msg)
                writeResult(data_obj, msg, idc+2, colNo=change_data_choiceNo+2, nowTime=excelObj.now,
                            timeNo=change_data_choiceNo+1, style='blue')
                successful_member += 1

            else:
                msg = '<失败>%s: 共有步骤：%d, 执行成功步骤：%d' % (data_obj.title, key_stepRowNo - 1, stepNo)
                print(msg)
                logging.info(msg)
                writeResult(data_obj, msg, idc + 2, colNo=change_data_choiceNo + 2, nowTime=excelObj.now,
                            timeNo=change_data_choiceNo + 1, style='red')

    if successful_member == target_member:
        msg = '<成功>%s, 共有条数：%d, 成功条数：%d'%(key_sheet_obj.title, target_member, successful_member)
        print(msg)
        logging.info(msg)
        writeResult(case_sheetObj, msg, rowNo, case_resultNo, excelObj.now, case_timeNo, style='blue')
    else:
        msg = '<失败>%s, 共有条数：%d, 成功条数：%d' % (key_sheet_obj.title, target_member, successful_member)
        print(msg)
        logging.info(msg)
        writeResult(case_sheetObj, msg, rowNo, case_resultNo, excelObj.now, case_timeNo, style='red')






if __name__ == '__main__':
    from testcases.TestLogin import testLogin
    testLogin()
    keySheetObj = excelObj.getSheet('修改资料')
    dataSheeObj = excelObj.getSheet('个人信息')
    changeInfo(keySheetObj, dataSheeObj, rowNo=3)
    getClose()
    getOpenLocalFile(excel_path)