# CHAPTER 11 모듈과 패키지

# 11.2.1 모듈 탐색 경로
import sys
for place in sys.path:
    print(place)

import sys
sys.path.insert(0, "/my/modules")

print()

# 11.2.2 상대/절대 경로 임포트

# 11.2.3 네임스페이스 패키지
from critters import wendigo, rougarou

# 11.2.4 모듈 vs 객체
import math
print(math.pi)
math.pi = 3.0
print(math.pi)

print()

# 11.3 파이썬 표준 라이브러리

# 11.3.1 누락된 키 처리하기: setdefault()와 defaultdict()
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)

from collections import defaultdict
def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)

print()

# 11.3.2 항목 세기: Counter()
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

print(breakfast_counter)

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)

print(breakfast_counter - lunch_counter)

print(lunch_counter - breakfast_counter)

print(breakfast_counter & lunch_counter)

print(breakfast_counter | lunch_counter)

print()

# 11.3.3 키 정렬하기: OrderedDict() # 파이썬 3.7 이전 버전 해당
quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!',
}
for stooge in quotes:
    print(stooge)

from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk'),
])

for stooge in quotes:
    print(stooge)

print()

# 11.3.4 스택 + 큐 == 데크
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))

def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('radar'))
print(another_palindrome('halibut'))

print()

# 11.3.5 코드 구조 순회하기: itertools
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# for item in itertools.cycle([1, 2]):
#     print(item)

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

def multyply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multyply):
    print(item)

print()

# 11.3.6 깔끔하게 출력하기: pprint()
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk'),
])

print(quotes)

pprint(quotes)

print()

# 11.3.7 임의값 얻기
from random import choice
print(choice([23, 9, 46, 'bacon', 0x123abc]))
print(choice(('a', 'one', 'and-a', 'two')))
print(choice(range(100)))
print(choice('alphabet'))

from random import sample
print(sample([23, 9, 46, 'bacon', 0x123abc], 3))
print(sample(('a', 'one', 'and-a', 'two'), 2))
print(sample(range(100), 4))
print(sample('alphabet', 7))

from random import randint
print(randint(38, 74))
print(randint(38, 74))
print(randint(38, 74))

from random import randrange
print(randrange(38, 74))
print(randrange(38, 74, 10))
print(randrange(38, 74, 10))

from random import random
print(random())
print(random())
print(random())
