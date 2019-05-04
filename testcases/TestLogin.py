from testcases.WriteTestResult import *
from testcases.ChangeInfo import changeInfo

def testLogin():
    executing_method = ''

    choices = excelObj.getValueByCol(case_sheetObj, case_choiceNo)
    for idx, choice in enumerate(choices[1:]):
        if choice.value == 'y':
            frame_type = excelObj.getValueByRow(case_sheetObj, idx + 2)[case_frameTypeNo].value
            if frame_type == "关键字":
                key_sheetName = excelObj.getValueByRow(case_sheetObj, idx + 2)[case_frameTypeNo + 1].value
                key_sheetObj = excelObj.getSheet(key_sheetName)

                key_rowNo = excelObj.getRowAndColNum(key_sheetObj)[0]

                stepNo = 0

                for step in range(2, key_rowNo + 1):
                    key_methodName = excelObj.getValueByRow(key_sheetObj, step)[key_methodNo].value
                    key_locType = excelObj.getValueByRow(key_sheetObj, step)[key_methodNo+1].value
                    key_loc = excelObj.getValueByRow(key_sheetObj, step)[key_methodNo+2].value
                    key_paramValue = excelObj.getValueByRow(key_sheetObj, step)[key_methodNo+3].value

                    if key_methodName and key_paramValue and key_locType is None and key_loc is None:
                        if isinstance(key_paramValue, int):
                            executing_method = key_methodName + '(%d)'%key_paramValue
                        else:
                            executing_method = key_methodName + '("%s")' % key_paramValue
                    if key_methodName and key_locType and key_loc and key_paramValue:
                        executing_method = key_methodName + str(tuple(key_locType.split(',')) + tuple(key_loc.split(',')) + tuple(key_paramValue.split(',')))
                    elif key_methodName and key_locType and key_loc and key_paramValue is None:
                        executing_method = key_methodName + str(tuple(key_locType.split(',')) + tuple(key_loc.split(',')))
                    elif key_methodName and key_locType is None and key_loc is None and key_paramValue is None:
                        executing_method = key_methodName + '()'

                    try:
                        eval(executing_method)
                        msg = '<成功> %s'%executing_method
                        print(msg)
                        writeResult(key_sheetObj, msg, step, key_resultNo, excelObj.now, key_timeNo,
                                    picPath=' ', picNo=key_picNo, style='blue')
                        stepNo += 1
                    except Exception as e:
                        msg = '<失败> %s' % executing_method
                        msg += str(e)
                        print(msg)
                        pic_path = '错误截图地址'
                        writeResult(key_sheetObj, msg, step, key_resultNo, excelObj.now, key_timeNo,
                                    picPath=pic_path, picNo=key_picNo, style='red')

                if stepNo == key_rowNo - 1:
                    msg = '<成功>%s, 共有步骤: %d，执行成功步骤: %d'%(key_sheetObj.title, key_rowNo-1, stepNo)
                    print(msg)
                    writeResult(case_sheetObj, msg, idx+2, case_resultNo, excelObj.now, case_timeNo, style='blue')

                else:
                    msg = '<失败>%s, 共有步骤: %d，执行成功步骤: %d' % (key_sheetObj.title, key_rowNo - 1, stepNo)
                    print(msg)
                    writeResult(case_sheetObj, msg, idx + 2, case_resultNo, excelObj.now,  case_timeNo, style='red')

            elif frame_type == '数据':
                data_key_sheetName = excelObj.getValueByRow(case_sheetObj, idx + 2)[case_frameTypeNo + 1].value
                data_key_sheetObj = excelObj.getSheet(data_key_sheetName)
                data_sheet_name = excelObj.getValueByRow(case_sheetObj, idx + 2)[case_frameTypeNo + 2].value
                data_sheetObj = excelObj.getSheet(data_sheet_name)
                changeInfo(data_key_sheetObj, data_sheetObj, rowNo=idx+2)

            # 清空不属于上述用例类型的结果及时间单元格
            else:
                writeResult(case_sheetObj, content=' ', rowNo=idx+2, colNo=case_resultNo, nowTime=' ', timeNo=case_timeNo)

        # 清空不需要执行的用例的结果及时间单元格
        else:
            writeResult(case_sheetObj, content=' ', rowNo=idx + 2, colNo=case_resultNo, nowTime=' ', timeNo=case_timeNo)


if __name__ == '__main__':
    testLogin()
    getClose()
