# CHAPTER 10 객체와 클래스

# 10.1 객체란 무엇인가?

# 10.2 간단한 객체

# 10.2.1 클래스 선언하기: class
class Cat():
    pass

class Cat:
    pass

a_cat = Cat()
another_cat = Cat()

# 10.2.2 속성
class Cat:
    pass

a_cat = Cat()
print(a_cat)
another_cat = Cat()
print(another_cat)

a_cat.age = 3
a_cat.name = "Mr. fuzzybuttons"
a_cat.nemesis = another_cat

print(a_cat.age)
print(a_cat.name)
print(a_cat.nemesis)

# a_cat.nemesis.name # AttributeError: 'Cat' object has no attribute 'name'

a_cat.nemesis.name = "Mr. Bigglesworth"
print(a_cat.nemesis.name)

print()

# 10.2.3 메서드

# 10.2.4 초기화
class Cat:
    def __init__(self, name):
        self.name = name

furball = Cat('Grumpy')

print('Our latest addition:', furball.name)

# 10.3 상속





