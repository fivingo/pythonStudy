# CHAPTER 12 데이터 길들이기

# 12.1 텍스트 문자열: 유니코드

# 12.1.1 파이썬 3 유니코드 문자열
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('A')

unicode_test('$')

unicode_test('\u00a2')

unicode_test('\u20ac')

unicode_test('\u2603')

place = 'cafe'
print(place)

import unicodedata
print(unicodedata.name('\u00e9'))

# print(unicodedata.lookup('E WITH ACUTE, LATIN SMALL LETTER'))
# "undefined character name 'E WITH ACUTE, LATIN SMALL LETTER'"

print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))

place = 'caf\u00e9'
print(place)
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlaut)
drink = 'Gew' + u_umlaut + 'rztramier'
print('Now I can finally have my', drink, 'in a', place)

print(len('$'))
print(len('\U0001f47b'))

print(chr(233))
print(chr(0xe9))
print(chr(0x1fc6))

print()

# 12.1.2 UTF-8

# 1byte: 아스키 코드
# 2byte: 키릴Cyrillc 문자를 제외한 대부분 파생된 라틴어
# 3byte: 기본 다국어 평면의 나머지
# 4byte: 아시아 언어 및 기호를 포함한 나머지

# 12.1.3 인코딩




