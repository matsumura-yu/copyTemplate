import xml.etree.ElementTree as ET

# xmlファイルの読み込み
tree = ET.parse('sample_srb.xml')

# 脆弱性を取得
items = tree.findall('issue-type-group/item')
for item in items:
    # 発見された脆弱性の数を取得
    count = item.get('count')
    # 脆弱性名の取得
    name = item.find('name').text
    print(name + ":" +count)