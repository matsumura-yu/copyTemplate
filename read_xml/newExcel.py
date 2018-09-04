import openpyxl
import glob
from xmlToJson import *

def sampleCreateExcel():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'test_sheet_1'
    wb.save('test.xlsx')
    glob.glob("*.xlsx")

# jsonからExcelのリストを作成
def jsonToListExcel():
    return

# dictionaryからリストを作成
def dictionaryToListExcel():
    xmlList = getAllXml()

    scenarioList = []
    for xmlFile in xmlList:
        scenario = createDictionary(xmlFile)
        scenarioList.append(scenario)
        
    # scenarioList:全シナリオの情報

    # excel生成
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'シナリオリスト'

    # 一番左上
    sheet['A1'] = '脆弱性/シナリオ'

    # 脆弱性の種類と件数を埋める
    for index, scenario in enumerate(scenarioList):
        print(str(index + 1) + "番目")
        print(scenario["scenarioName"])

        # シナリオ名記述
        sheet.cell(row = 1, column = (index + 2)).value = scenario["scenarioName"]

        # 脆弱性名挿入
        # 重複したとき用に脆弱性のリストを作成
        vulsList = []

        for vuls_index, vuls in enumerate(scenario["vuls"]):
            vulsList.append(vuls["vulName"])
            sheet.cell(row = vuls_index + 2, column = 1).value = vuls["vulName"]
            sheet.cell(row = vuls_index + 2, column = 2).value = vuls["count"]
            sheet.cell(row = vuls_index + 2, column = 2).data_type = 'n'
        print(vulsList)
    wb.save('list.xlsx')


# レポートのエクセルを作成
def createReportExcel():
    return


dictionaryToListExcel()