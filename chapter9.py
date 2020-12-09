# CHAPTER 9 함수

# 9.1 함수 정의하기: def
def do_nothing():
    pass

# 9.2 함수 호출하기: ()
do_nothing()

def make_a_sound():
    print('quack')
make_a_sound()

def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected')

print()

# 9.3 인수와 매개변수
def echo(anything):
    return anything + ' ' + anything

print(echo('Rumplestilskin'))

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper"
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color "  + color + "."

print(commentary('blue'))

print(do_nothing())

print()

# 9.3.1 유용한 None
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

thing = None
if thing is None:
    print("It's a nothing")
else:
    print("It's something")

def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")

whatis(None)
whatis(True)
whatis(False)

whatis(0)
whatis(0.0)
whatis('')
whatis("")
whatis('''''')
whatis(())
whatis([])
whatis({})
whatis(set())
whatis(0.00001)
whatis([0])
whatis([''])
whatis(' ')

print()

# 9.3.2 위치 인수
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))

print(menu('beef', 'bagel', 'bordeaux'))

print()

# 9.3.3 키워드 인수
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

print(menu('frontenac', dessert='flan', entree='fish'))

print()

# 9.3.4 기본 매개변수 값 지정하기
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))

print(menu('dunkelfelder', 'duck', 'doughnut'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')

def works(arg):
    result = []
    result.append(arg)
    return result
print(works('a'))
print(works('b'))

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')

print()

# 9.3.5 위치 인수 분해하기/모으기: *
def print_args(*args):
    print('Positional tuple:', args)

print_args()

print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Nedd this one:', required1)
    print('Nedd this one. too:', required2)
    print('All the rest:', args)
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

print_args(2, 5, 7, 'x')
args = (2, 5, 7, 'x')
print_args(args)
print_args(*args)

# 함수 외부에서 *args는 튜플 인수를 쉼표로 구분된 위치 매개변수로 분해한다.
# 함수 내부에서 *args는 모든 위치의 인수를 단일 인수 튜플로 수집한다.

print()

# 9.3.6 키워드 인수 분해하기/모으기: *
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# 키워드 인수를 함수에 전달하면, 함수 내 키워드 매개변수와 일치한다.
# 딕셔너리 인수를 함수에 전달하면 함수 내 딕셔너리 매개변수가 있다.
# 하나 이상의 키워드 인수(이름=값)를 함수에 전달하고, 이름 **kwargs에 수집하여, kwargs 딕셔너리 매개변수로 해석할 수 있다.
# 함수 외부에서 **kwargs는 딕셔너리 kwargs를 '이름=값' 인수로 분해한다.
# 함수 내부에서 **kwargs는 '이름=값' 인수를 단일 딕셔너리 매개변수 kwagrs에 모은다.

print()

# 9.3.7 키워드 전용 인수
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)
data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print_data(data, start=4)
print_data(data, end=2)

print()

# 9.3.8 가변/불변 인수
outside = ['one', 'fine', 'day']
def mangle(arg):
    arg[1] = 'trrible'
print(outside)
mangle(outside)
print(outside)

print()

# 9.4 독스트링
def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The opration is:
        1. Check wheather the *second* argument is ture.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

help(echo)

print(echo.__doc__)

print()

# 9.5 일등 시민: 함수
def answer():
    print(42)

answer()

def run_something(func):
    func()

run_something(answer)

print(type(run_something))

def add_args(arg1, arg2):
    print(arg1 + arg2)

print(type(add_args))

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))

print()

# 9.6 내부 함수
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)
print(outer(4, 7))

def knights(saying):
    def inner(quote):
        return "We are the kinght who say: '%s'" % quote
    return inner(saying)
print(knights('Ni!'))

print()

# 9.6.1 클로저

# inner2()는 인수를 취하지 않고, 외부 함수의 변수를 직접적으로 사용한다.
# knight2()는 inner2 함수 이름을 호출하지 않고, 이를 반환한다.

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))

print(a)
print(b)

print(a())
print(b())

print()

# 9.7 익명 함수: lambda

# words: 리스트
# func: 리스트의 각 word 문자열에 적용되는 함수

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')

# 9.8 제너레이터






