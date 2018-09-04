import xml.etree.ElementTree as ET

# xmlファイルの読み込み
tree = ET.parse('sample_srb.xml')

# Dictionaryの初期化
dictList = {}

# 脆弱性を取得
items = tree.findall('issue-type-group/item')
for item in items:
    # 発見された脆弱性の数を取得
    count = item.get('count')
    # 脆弱性名の取得
    name = item.find('name').text
    # print(name + ":" +count)

    # 脆弱性名:検知数    
    dictList[name] = count



# タプルのリストが返る
print(dictList.items())


# 表左に書くname, 値count
# def createSheet(name, count):

print("------------")

# シナリオ名の取得
scenario = tree.find('scan-information/scan-name').text
print(scenario)




# 1シナリオの構造をjsonにするメソッド
def createJson(xmlfile):
    print("---")