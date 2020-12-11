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

