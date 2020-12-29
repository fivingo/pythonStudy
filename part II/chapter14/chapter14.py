# CHAPTER 14 파일과 디렉터리

# 14.1 파일 입출력

# 14.1.1 생성하기/열기: open()
# fileobj = open(filename, mode)

fout = open('oops.txt', 'wt')
fout.close()

# 14.1.2 텍스트 파일 쓰기: print()
fout = open('oops.txt', 'wt')
print('Oops, I created a file', file=fout)
fout.close()

# 14.1.3 텍스트 파일 쓰기: write()
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
print(len(poem))

fout = open('relativity.txt', 'wt')
print(fout.write(poem))
fout.close()

fout = open('relativity.txt', 'wt')
print(poem, file=fout)
fout.close()

fout = open('relativity.txt', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity.txt', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(poem[offset:offset + chunk]))
    offset += chunk
fout.close()

# fout = open('relativity.txt', 'xt') # FileExistsError: [Errno 17] File exists: 'relativity.txt'
try:
    fout = open('relativity.txt', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity.txt already exists! That was a close one.')

print()

# 14.1.4 텍스트 파일 읽기: read(), readline(), readlines()
fin = open('relativity.txt', 'rt')
poem = fin.read()
fin.close()
print(len(poem))

poem = ''
fin = open('relativity.txt', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print(len(poem))

poem = ''
fin = open('relativity.txt', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))

poem = ''
fin = open('relativity.txt', 'rt')
for line in fin:
    poem += line
fin.close()
print(len(poem))

fin = open('relativity.txt', 'rt')
lines = fin.readline()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')

print()

# 14.1.5 이진 파일 쓰기: write()
bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile.txt', 'wb')
print(fout.write(bdata))
fout.close()

fout = open('bfile.txt', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(bdata[offset:offset + chunk]))
    offset += chunk

print()

# 14.1.6 이진 파일 읽: read()
fin = open('bfile.txt', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

print()

# 14.1.7 자동으로 파일 닫기: with
with open('relativity.txt', 'wt') as fout:
    fout.write(poem)

# 14.1.8 파일 위치 찾기: seek()
fin = open('bfile.txt', 'rb')
print(fin.tell())

print(fin.seek(255))

bdata = fin.read()
print(len(bdata))
print(bdata[0])

import os
print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)

fin = open('bfile.txt', 'rb')

print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin = open('bfile.txt', 'rb')

print(fin.seek(254, 0))
print(fin.tell())

print(fin.seek(1, 1))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

print()

# 14.2 메모리 매핑




