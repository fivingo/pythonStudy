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














