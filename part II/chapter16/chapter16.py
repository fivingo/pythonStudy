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
menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

import datetime
import json
now = datetime.datetime.utcnow()
print(now)
# json.dumps(now)

now_str = str(now)
print(json.dumps(now_str))
from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

import datetime
now = datetime.datetime.utcnow()
class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance() checks the type of obj
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # else it's something the normal decoder knows:
        return json.JSONEncoder.default(self, obj)
print(json.dumps(now, cls=DTEncoder))

import datetime
now = datetime.datetime.utcnow()
print(type(now))
print(isinstance(now, datetime.datetime))
print(type(234))
print(isinstance(234, int))
print(type('hey'))
print(isinstance('hey', str))

import datetime
import json
now = datetime.datetime.utcnow()
print(json.dumps(now, default=str))

print()

# 16.3.6 YAML

# import yaml
# with open('mcintyre.yaml', 'rt') as fin:
#     text = fin.read()
# data = yaml.load(text)
# print(data['details'])
# print(len(data['poems']))

# print(data['poems'][1]['title'])

# 16.3.7 Tablib

# 16.3.8 판다스

import pandas
data = pandas.read_csv('chapter16/villains.csv')
print(data)

import pandas
dates = pandas.date_range('2021-01-01', periods=3, freq='MS')
print(dates)

print()

# 16.3.9 설정 파일

# import configparser
# cfg = configparser.ConfigParser()
# print(cfg.read('chapter16/settings.cfg'))
# print(cfg)
# cfg['french']
# cfg['french']['greeting']
# cfg['files']['bin']

# 16.4 이진 파일

# 16.4.1 패디드 아진 파일과 메모리 매핑

# 16.4.2 스프레드시트

# 16.4.3. HDF5

# 16.4.4 TileDB

# 16.5 관계형 데이터베이스
