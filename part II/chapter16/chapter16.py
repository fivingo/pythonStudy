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

