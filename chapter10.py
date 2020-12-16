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

print()

# 10.3 상속

# 10.3.1 부모 클래스 상속받기
class Car():
    pass

class Yugo(Car):
    pass

print(issubclass(Yugo, Car))

give_me_a_car = Car()
give_me_a_yugo = Yugo()

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

print()

# 10.3.2 메서드 오버라이드
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

print()

# 10.3.3 메서드 추가하기
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()

# give_me_a_car.need_a_push() # AttributeError: 'Car' object has no attribute 'need_a_push'

print()

# 10.3.4 부모에게 도움받기: super()
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print(bob.name)
print(bob.email)

class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email

print()

# 10.3.5 다중 상속
class Animal:
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())

print()

# 10.3.6 믹스인
class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))
class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()

print()

# 10.4 자신: self
a_car = Car()
a_car.exclaim()

Car.exclaim(a_car)

print()

# 10.5 속성 접근

# 10.5.1 직접 접근
class Duck:
    def __init__(self, input_name):
        self.name = input_name

fowl = Duck('Daffy')
print(fowl.name)

fowl.name = 'Daphne'
print(fowl.name)

print()

# 10.5.2 Getter/Setter 메서드
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

don = Duck('Donald')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())

print()

# 10.5.3 속성 접근을 위한 프로퍼티
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

don = Duck('Donald')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())

don = Duck('Donald')
print(don.name)
don.name = 'Donna'
print(don.name)

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)

print()

# 10.5.4 계산된 값의 프로퍼티
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)

print(c.diameter)

c.radius = 7
print(c.diameter)

# c.diameter = 20 # AttributeError: can't set attribute

print()

# 10.5.5 프라이버스를 위한 네임 맹글링
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)

# fowl.__name # AttributeError: 'Duck' object has no attribute '__name'

print(fowl._Duck__name)

print()

# 10.5.6 클래스와 객체 속성
class Fruit:
    color = 'red'

blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)

blueberry.color = 'blue'
print(blueberry.color)
print(Fruit.color)

Fruit.color = 'orange'
print(Fruit.color)
print(blueberry.color)
new_fruit = Fruit()
print(new_fruit.color)

print()

# 10.6 메서드 타입

# 10.6.1 인스턴스 메서드

# 10.6.2 클래스 메서드
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

print()

# 10.6.3 정적 메서드
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')
CoyoteWeapon.commercial()

print()

# 10.7 덕 타이핑
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

class BabbingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babbie'

brook = BabbingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)

print()

# 10.8 매직 매서드
class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('Ha')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('Ha')
third = Word('eh')
print(first == second)
print(first == third)

first = Word('ha')
print(first)

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("' + self.text + '")'

first = Word('ha')
print(first.__repr__())
print(first)

print()

# 10.9 애그리게이션과 콤퍼지션
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')

a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()

print()

# 10.10 객체는 언제 사용할까?
'''
- 비슷한 행동(메서드)을 하지만 내부 상태(속성)가 다른 개별 인스터슨가 필요할 때, 객체는 매우 유용하다.
- 클래스는 상속을 지우너하지만, 모듈은 상속을 지원하지 않는다.
- 어떤 한 가지 일만 수행한다면 모듈이 가장 좋은 선택일 것이다. 프로그램에서 파이썬 모듈이 참조된 횟수에 상관없이
  단 하나의 복사본만 불러온다(자바와 C++ 개발자는 파이썬 모듈을 싱글톤처럼 쓸수있다).
- 여러 함수에 인수로 전달하는 여러 변수가 있다면, 클래스를 정희하는 것이 더 좋다. 예를 들어 화상 이미지를 나타내기 위해
  size나 color를 딕셔너리의 키로 사용한다고 가정해보자. 프로그램에서 각 이미지에 대한 딕셔너리를 생성하고,
  scale()과 transform() 같은 함수에 인수를 전달할 수 잇다. 키와 함수를 추가하면 코드가 지저분해질 수도 있다.
  size와 color 속성으로하고 scale()과 transform()을 메서드를 하는 이미지 클래스를 정하는 것이 더 일관성이 있다.
  색상 이미지에 대한 모든 데이터와 메서드를 한 곳에 정의 할 수 있기 때문이다.
- 가장 간단한 문제 해결법을 사용한다. 딕셔너리, 리스트, 튜플은 모듈보다 더 작고 간단하며 빠르다.
  그리고 일반적으로 모듈은 클래스보다 더 간단하다.
'''

# 10.11 네임드 튜플
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

duck2 = Duck(bill = 'wide orange', tail = 'long')

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)

duck_dict['color'] = 'green'
print(duck_dict)

# duck.color = 'green' # AttributeError: 'Duck' object has no attribute 'color'

print()

# 10.12 데이터 클래스
class TeenyClass():
    def __init__(self, name):
        self.name = name

teeny = TeenyClass('itsy')
print(teeny.name)

from dataclasses import dataclass
@dataclass
class TeenyDataClass:
    name: str

teeny = TeenyDataClass('bitsy')
print(teeny.name)

from dataclasses import dataclass
@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
print(snowman)
print(duck)

print(duck.habitat)
print(snowman.teeth)
