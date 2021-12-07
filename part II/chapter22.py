# CHAPTER 22 파이 과학

# 22.1 수학 및 통게 표준 라이브러리

# 22.1.1 math 함수

import math
print(math.pi)
print(math.e)

print(math.fabs(98.6))
print(math.fabs(-271.1))

print(math.floor(98.6))
print(math.floor(-271.1))
print(math.ceil(98.6))
print(math.ceil(-271.1))

print(math.factorial(0))
print(math.factorial(1))
print(math.factorial(2))
print(math.factorial(3))
print(math.factorial(10))

print(math.log(1.0))
print(math.log(math.e))

print(math.log(8, 2))

print(math.pow(2, 3))

print(2 ** 3)
print(2.0 ** 3)

print(math.sqrt(100.0))

# print(math.sqrt(-100.0))

x = 3.0
y = 4.0
print(math.hypot(x, y))

print(math.sqrt(x * y + y * y))
print(math.sqrt(x ** 2 + y ** 2))

print(math.radians(180.0))
print(math.degrees(math.pi))

print()

# 22.1.2 복소수 계산

# 22.1.3 정확한 부동소수점 계산하기: decimal

from decimal import Decimal
price = Decimal('19.99')
tax = Decimal('0.06')
total = price + (price * tax)
print(total)

penny = Decimal('0.01')
print(total.quantize(penny))

print()

# 22.1.4 유리수 계산하기: fractions

from fractions import Fraction
print(Fraction(1,3) * Fraction(2, 3))

print(Fraction(1.0 / 3.0))
print(Fraction(Decimal('1.0') / Decimal('3.0')))

import fractions
# print(fractions.gcd(24, 16))

print()

# 22.1.5 설정된 시퀀스 사용하기: array

# 22.1.6 간단한 통계 처리하기: statistics

# 22.1.7 행렬 곱하기

# 22.2 과학과 파이썬

# 22.3 넘파이

# 22.3.1 배열 만들기(1): array()

