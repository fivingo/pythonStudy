# CHAPTER 16 파일과 데이터베이스

# 16.1 플랫 텍스트 파일

# 16.2 패디드 텍스트 파일

# 16.3 표 형식 텍스트 파일

# 16.3.1 CSV

import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
]
with open('chapter16/villains', 'wt') as fout: # a context manager
    csvout = csv.writer(fout)
    csvout.writerows(villains)

import csv
with open('chapter16/villains', 'rt') as fin: # 컨텍스트 매니저
    cin = csv.reader(fin)
    villains = [row for row in cin] # 리스트 컴프리헨션
print(villains)

print()

import csv
with open('chapter16/villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]
print(villains)

print()

import csv
villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
]
with open('chapter16/villains.txt', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

import csv
with open('chapter16/villains.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
print(villains)

print()

# 16.3.2 XML

import xml.etree.ElementTree as et
tree = et.ElementTree(file='chapter16/menu.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
print(len(root))    # menu의 하위 태그 수
print(len(root[0])) # breakfast의 item 수

print()

# 16.3.3 XML 보안 노트

# 보안되지 않은 parse
from xml.etree.ElementTree import parse
et = parse('chapter16/menu.xml')
# 보안된 parse
from defusedxml.ElementTree import parse
et = parse('chapter16/menu.xml')

# 16.3.4 HTML

# 16.3.5 JSON

menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }

import json
menu_json = json.dump(menu)
print(menu_json)

