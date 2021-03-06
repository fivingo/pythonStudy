# CHAPTER 8 딕셔너리와 셋

# 8.1 딕셔너리

# 8.1.1 생성하기: {}
empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A perid of twenty-four hours, mostly miispent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)

print()

# 8.1.2 생성하기: dict()
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)
print()

# 8.1.3 변환하기: dict()
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

print()

# 8.1.4 항목 추가/변경: [key]
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

pythons['Gilliam'] = 'Gerry'
print(pythons)

pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}
print(some_pythons)

print()

# 8.1.5 항목 얻기: [key]와 get()
print(some_pythons['John'])
print('Groucho' in some_pythons)
print(some_pythons.get('John'))
print(some_pythons.get('Groucho', 'Not a Python'))
print(some_pythons.get('Groucho'))

print()

# 8.1.6 모든 키 얻기: keys()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
print(list(signals.keys()))

print()

# 8.1.7 모든 값 얻기: values()
print(list(signals.values()))

print()

# 8.1.8 모든 키-값 얻기: items()
print(list(signals.items()))

print()

# 8.1.9 길이 얻기: len()
print(len(signals))

print()

# 8.1.10 결합하기: (**a, **b)
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})

third = {'d': 'donuts'}
print({**first, **third, **second})

print()

# 8.1.11 결합하기: update()
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)

print()

# 8.1.12 키와 del로 항목 삭제하기
del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

print()

# 8.1.13 키로 항목 가져온 뒤 삭제하기: pop()
print(len(pythons))
print(pythons.pop('Palin'))
print(len(pythons))
#print(pythons.pop('Palin'))
print(pythons.pop('First', 'Hugo'))
print(len(pythons))

print()

# 8.1.14 모든 항목 삭제하기: clear()
pythons.clear()
print(pythons)
pythons = {}
print(pythons)

print()

# 8.1.15 키 멤버십 테스트: in
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
print('Chapman' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)

print()

# 8.1.16 할당하기: =
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(signals)

print()

# 8.1.17 얕은 복사: copy()
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

print()

# 8.1.18 깊은 복사: deepcopy()
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile']
}
signals_copy = signals.copy()
print(signals)
print(signals_copy)

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

import copy
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile']
}
signals_copy = copy.deepcopy(signals)
print(signals)
print(signals_copy)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

print()

# 8.1.19 딕셔너리 비교
a = {1: 1, 2: 2, 3: 3}
b = {3: 3, 1: 1, 2: 2}
print(a == b)
#print(a <= b)

a = {1: [1, 2], 2: [1], 3: [1]}
b = {1: [1, 1], 2: [1], 3: [1]}
print(a == b)

print()

# 8.1.20 순회하기: for와 in
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

print()

# 8.1.21 딕셔너리 컴프리헨션
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

vowels = 'aeiou'
word = 'onomatopoeia'
vowels_count = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowels_count)

print()

# 8.2 셋

# 8.2.1 생성하기: set()
empty_set = set()
print(empty_set)
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

print()

# 8.2.2 변환하기: set()
print(set('letters'))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

print()

# 8.2.3 길이 얻기: len()
reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))

print()

# 8.2.4 항목 추가하기: add()
s = set((1, 2, 3))
print(s)
s.add(4)
print(s)

print()

# 8.2.5 항목 삭제하기: remove()
s = set((1, 2, 3))
s.remove(3)
print(s)

print()

# 8.2.6 순회하기: for와 in
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

print()

# 8.2.7 멤버십 테스트: in
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhatten': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

print()

# 8.2.8 콤비네이션과 연산자
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}
print(a & b)
print(a.intersection(b))

print(bruss & wruss)

print(a | b)
print(a.union(b))

print(bruss | wruss)

print(a - b)
print(a.difference(b))

print(bruss - wruss)
print(wruss - bruss)

print(a ^ b)
print(a.symmetric_difference(b))

print(bruss ^ wruss)

print(a <= b)
print(a.issubset(b))

print(bruss <= wruss)

print(a <= a)
print(a.issubset(a))

print(a < b)
print(a < a)
print(bruss < wruss)

print(a >= b)
print(a.issubset(b))
print(wruss >= bruss)

print(a >= a)
print(a.issubset(a))

print(a > b)
print(wruss > bruss)

print(a > a)

print()

# 8.2.9 셋 컴프리헨션
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

print()

# 8.2.10 불변 셋 생성하기: frozenset()
print(frozenset([3, 2, 1]))
#print(frozenset(set([2, 1, 3]))
print(frozenset({3, 1, 2}))
print(frozenset((2, 3, 1)))

fs = frozenset([3, 2, 1])
print(fs)
#fs.add(4)

# 8.3 지금까지 배운 자료구조

# 대괄호 []를 사용한 리스트
# 콤마와 괄호 ()를 사용한 튜플 (괄호는 옵션이다)
# 중괄호 {}를 사용한 딕셔너리 또는 셋

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}

print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])
print('Harpo' in marx_list)
print('Harpo' in marx_tuple)
print('Harpo' in marx_dict)
print('Harpo' in marx_set)

print()

# 8.4 자료구조 결합하기
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)

list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)

houses = {(44.79, -93.14, 285): 'My House', (38.89, -7703, 13): 'The White House'}
