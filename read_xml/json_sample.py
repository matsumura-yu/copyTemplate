import json

def create_json():
    dic = {
        "profile1": {
            "first" : "Taro",
            "last" : "Yamada"
        },
        "profile2": {
            "first": "Hanako",
            "last": "Yamada"
        }
    }

    a = open('sample.json', 'w')
    json.dump(dic, a, indent=4)

def open_json():
    a = open('sample.json')
    b = json.load(a)
    

    print(b)
    print(b.keys())
    # 辞書に対してもlenは使える
    # その際一番上層の数のみ抽出
    print(len(b))
    print(len(b.keys()))
    print(b.keys())

def create_listjson():
    list = []
    list.append("d")
    list.append("a")

    dict = {
        "profile1": {
            "first" : "Taro",
            "last" : "Yamada"
        }
    }

    list.append(dict)
    print(list)
    print("--------------")


    dict2 = {
        "scenario1" : 
        {
            "name" : "シナリオ１登録",
            "vuls" : [{
                "name" : "ヘッダーなし",
                "count" : 2
            },
            {
                "name" : "aaa",
                "count" : 3
            }]
        }
    }

    print(dict2)
    print("シナリオ１")
    print(dict2['scenario1']['vuls'][0])

    vulsdict = {"name": "シナリオ２", "count" : 3}
    dict2['scenario1']['vuls'].append(vulsdict)

    print("--------------")
    print(dict2)

    a = open('sample.json', 'w')
    json.dump(dict2, a, indent=4)

    # c = open('sample.json')
    # b = json.load(c)

    # print(b)


def copyJson():
    a = open('scenario.json', encoding="utf-8")
    b = json.load(a)
    a.close()
    print(b)

    c = open('copy.json', 'w', encoding="utf-8")

    # ensure_ascii=Falseをつけてuの文字化け回避
    json.dump(b, c, indent=4, ensure_ascii=False)
    c.close()

    
# create_listjson()
copyJson()