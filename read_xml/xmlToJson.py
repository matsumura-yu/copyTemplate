import xml.etree.ElementTree as ET
import json

# 1シナリオの情報をjson保存
def createJson():
    # xmlファイルの読み込み
    tree = ET.parse('sample_srb1.xml')

    # 脆弱性の配列
    vuls = []

    # 脆弱性の情報
    # 参照渡しのためfor文↑で書くと毎回このデータを書き換えに行って一番最後の書き換えで更新される
    # vulInfo = {"vulName" : "", "count" : 0}

    # シナリオ名の取得

    # 脆弱性のリストを取得
    items = tree.findall('issue-type-group/item')
    for item in items:

        # 脆弱性の情報
        vulInfo = {"vulName" : "", "count" : 0}

        # 脆弱性名の取得
        name = item.find('name').text
        # 脆弱性の件数を取得
        count = item.get('count')
        
        vulInfo["vulName"] = name
        vulInfo["count"] = count
        print('----------')
        print(name)
        print(vulInfo)

        vuls.append(vulInfo)
        print('----------')
        print(vuls)
        

    print(vuls)

    scenario = {"scenarioName": "test", "vuls": vuls}

    print(scenario)

    a = open('scan.json', 'w', encoding="utf-8")
    json.dump(scenario, a, indent = 4, ensure_ascii = False)
    a.close()



createJson()