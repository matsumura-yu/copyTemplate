"""
wlist = ['apple', 'orange', 'バナナ', 'リンゴ', 'オレンジ']
word = 'バナナ'

# print(word in wlist)

# forの中のforではindexがどうなっているか

secList = ['ボブ','test' , 'さとう', 'アリス', 'チャーリー']

for index, item in enumerate(wlist):
    print(str(index) + '番目です')
    # index = 0
    # print(str(index) + "： " + "０を代入した結果")

    for sec_index, sec_item in enumerate(secList):
        print('--------ループ２----------')
        print(index)
        print(item)
        print(sec_index)
        print(sec_item)
        print('---------')

"""

# 一度テンプレートに載ってる脆弱性を一覧にする
# どのテンプレートシートのどの場所にあったかを保存する
import openpyxl

templateBook = openpyxl.load_workbook('template.xlsx')
templateSheet = templateBook['template']

for row in templateSheet.rows:
    if row[2].value == None or row[2].value == '脆弱性分類':
        continue
    print(row[2].value)
    print(row[2].row)
    print(row[2].column)