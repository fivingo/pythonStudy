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
snowman = '\u2603'

print(len(snowman))

ds = snowman.encode('utf-8')

print(len(ds))
print(ds)

# ds = snowman.encode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode character '\u2603' in position 0: ordinal not in range(128)

print(snowman.encode('ascii', 'ignore'))

print(snowman.encode('ascii', 'replace'))

print(snowman.encode('ascii', 'backslashreplace'))

print(snowman.encode('ascii', 'xmlcharrefreplace'))

print()

# 12.1.4 디코딩
place = 'caf\u00e9'
print(place)
print(type(place))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)

# place3 = place_bytes.decode('ascii')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)

place4 = place_bytes.decode('latin-1')
print(place4)

place5 = place_bytes.decode('windows-1252')
print(place5)

print()

# 12.1.5 HTML 엔티티
import html
print(html.unescape("&egrave;"))

print(html.unescape("&#233;"))
print(html.unescape("&#xe9;"))

from html.entities import html5
print(html5["egrave"])
print(html5["egrave;"])

char = '\u00e9'
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])

place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value)
print(byte_value.decode())

print()

# 12.1.6 정규화
eacute1 = 'é'       # UTF-8
eacute2 = '\u00e9'  # 유니코드 코드 포인트
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}' # 유니코드 이름
eacute4 = chr(233)    # 10진수 바이트 값
eacute5 = chr(0xe9)   # 16진수 바이트 값
print(eacute1, eacute2, eacute3, eacute4, eacute5)
print(eacute1 == eacute2 == eacute3 == eacute4 == eacute5)

import unicodedata
print(unicodedata.name(eacute1))
print(ord(eacute1))
print(0xe9)

eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"
print(eacute_combined1, eacute_combined2, eacute_combined3)
print(eacute_combined1 == eacute_combined2 == eacute_combined3)
print(len(eacute_combined1))

print(eacute1 == eacute_combined1)

eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)
print(len(eacute_normalized))
print(eacute_normalized == eacute1)
print(unicodedata.name(eacute_normalized))

print()

# 12.2 정규 표현식
import re
result = re.match('You', 'Young Frankenstein')

youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')

# 12.2.1 시작부터 일치하는 패턴 찾기: match()
import re
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())
m = re.match('^You', source)
if m:
    print(m.group())

m = re.match('Frank', source)
if m:
    print(m.group())

if m := re.match('Frank', source):
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m:
    print(m.group())

print()

# 12.2.2 첫 번째 일치하는 패턴 찾기: search()
import re
source = 'Young Frankenstein'
m = re.search('Frank', source)
if m:
    print(m.group())

print()

#12.2.3 일치하는 모든 패턴 찾기: findall()
m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

m = re.findall('n.', source)
print(m)

m = re.findall('n.?', source)
print(m)

print()

# 12.2.4 패턴으로 나누기: split()
m = re.split('n', source)
print(m)

print()

# 12.2.5 일치하는 패턴 대체하기: sub()
m = re.sub('n', '?', source)
print(m)

print()

# 12.2.6 패턴: 특수 문자
import string
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

print(re.findall('\d', printable))

print(re.findall('\w', printable))

print(re.findall('\s', printable))

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall('\w', x))

print()

# 12.2.7 패턴: 지정자
source = '''I wish I may, I wish I might
    Have a dish of fish tonight.'''

print(re.findall('wish', source))

print(re.findall('wish|fish', source))

print(re.findall('^wish', source))

print(re.findall('^I wish', source))

print(re.findall('fish$', source))

print(re.findall('fish tonight.$', source))

print(re.findall('fish tonight\.$', source))

print(re.findall('[wf]ish', source))

print(re.findall('[wsh]+', source))

print(re.findall('ght\W', source))

print(re.findall('I (?=wish)', source))

print(re.findall('(?<=I) wish', source))

print(re.findall('\bfish', source))

print(re.findall(r'\bfish', source))

print()

# 12.2.8 패턴: 매칭 결과 지정하기
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))

print()

# 12.3 이진 데이터

# 12.3.1 바이트와 바이트 배열
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)

print(b'\x61')
print(b'\x01abc\xff')

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
# the_bytes[1] = 127 # TypeError: 'bytes' object does not support item assignment

blist = [1, 2, 3, 255]
the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)

the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))

print(the_bytes)

print()

# 12.3.2 이진 데이터 변환하기: struct
import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

print(data[16:20])
print(data[20:24])

print(0x9a)
print(0x8d)

print(struct.pack('>L', 154))
print(struct.pack('>L', 141))

print(struct.unpack('>2L', data[16:24]))

print(struct.unpack('>16x2L6x', data))

print()

# 12.3.3 기타 이진 데이터 도구

# 12.3.4 바이트/문자열 변환하기: binacsii()
import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))

print(binascii.unhexlify(b'98504e470d0a1a0a'))

print()

# 12.3.5 비트 연산자
