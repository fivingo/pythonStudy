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




