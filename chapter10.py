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

















