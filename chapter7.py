# 7.1 튜플 #

# 7.1.1 튜플 생성하기: , 그리고 ()

empty_tuple = ()
print(empty_tuple)

print()

one_marx = 'Groucho',
print(one_marx)

print()

one_marx = ('Groucho',)
print(one_marx)

print()

one_marx = ('Groucho')
print(one_marx)
print(type(one_marx))

print()

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

print()

one_marx = 'Groucho',
print(type(one_marx))
print(type('Groucho',))
print(type(('Groucho',)))

print()

marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a)
print(b)
print(c)

print()

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)

print()

# 7.1.2 생성하기: tuple()
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

print()

# 7.1.3 결합하기: +
temp = ('Groucho',) + ('Chico', 'Harpo')
print(temp)

print()

# 7.1.4 항목 복제하기: *
temp = ('yada',) * 3
print(temp)

print()

# 7.1.5 비교하기
a = (7, 2)
b = (7, 2, 9)
print(a == b)
print(a <= b)
print(a < b)

print()

# 7.1.6 순회하기: for와 in
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)

print()

# 7.1.7 수정하기
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(t1 + t2)

print()

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
t1 += t2
print(t1)

print()

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1))
t1 += t2
print(id(t1))

print()

# 7.2 리스트 #

# 7.2.1 생성하기: []
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Tursday', 'Friday']
big_birds = ['emu', 'ostrich', 'casswary']
first_names = ['Grahmam', 'John', 'Terry', 'Micheal']
leap_years = [2000, 2004, 2008]
randomess = ['Punxsatawney', {"groundhog": "Phil"}, "Feb. 2"]

# 7.2.2 생성 및 변환하기: list()
another_empty_list = list()
print(another_empty_list)

print()

print(list('cat'))

print()

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

print()

# 7.2.3 문자열 분할로 생성하기: split()
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))

print()

splitme = 'a/b//c/d///e'
print(splitme.split('/'))

print()

splitme = 'a/b//c/d///e'
print(splitme.split('//'))

print()

# 7.2.4 [offset]으로 항목 얻기
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])

print()

print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

print()

# 7.2.5  슬라이스로 항목 얻기
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print((marxes[::2]))
print((marxes[::-2]))
print((marxes[::-1]))

marxes.reverse()
print(marxes)

print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])

print()

# 7.2.6 리스트 끝에 항목 추가하기: append()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)

print()

# 7.2.7 오프셋과 insert() 항목 추가하기
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo')
print(marxes)

print()

# 7.2.8 모든 항목 복제하기: *
print(["blah"] * 3)

print()

# 7.2.9 리스트 병합하기: extend()와 +
marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

print()

marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

print()

marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

print()

# 7.2.10 [offset]으로 항목 바꾸기
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

print()

# 7.2.11 슬라이스로 항목 바꾸기
numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)

print()

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)
numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)

print()

numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers)

print()

numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers)

print()

# 7.2.12 오프셋으로 항목 삭제하기: del
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(marxes[-1])
del marxes[-1]
print(marxes)

print()

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes)

print()

# 7.2.13 값으로 항목 삭제하기: remove()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)

print()

# 7.2.14 오프셋으로 항목을 얻은 후 삭제하기: pop()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)

print()

# 7.2.15 모든 항목 삭제하기: clear()
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)

print()

# 7.2.16 값으로 오프셋 찾기: index()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

print()

simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))

print()

# 7.2.17 존재여부 확인하기: in
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)

print()

words = ['a', 'deer', 'a', 'female', 'deer']
print('deer' in words)

print()

# 7.2.18 값 세기: count()
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

print()

# 7.2.19 문자열로 변환하기: join()
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))

print()

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)

print()

# 7.2.20 정렬하기: sort()와 sorted()
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)

print()

marxes.sort()
print(marxes)

print()

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

print()

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)

print()




