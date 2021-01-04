# # CHAPTER 14 파일과 디렉터리
#
# # 14.1 파일 입출력
#
# # 14.1.1 생성하기/열기: open()
# # fileobj = open(filename, mode)
#
# fout = open('oops.txt', 'wt')
# fout.close()
#
# # 14.1.2 텍스트 파일 쓰기: print()
# fout = open('oops.txt', 'wt')
# print('Oops, I created a file', file=fout)
# fout.close()
#
# # 14.1.3 텍스트 파일 쓰기: write()
# poem = '''There was a young lady named Bright,
# Whose speed was far faster than light;
# She started one day
# In a relative way,
# And returned on the previous night.'''
# print(len(poem))
#
# fout = open('relativity.txt', 'wt')
# print(fout.write(poem))
# fout.close()
#
# fout = open('relativity.txt', 'wt')
# print(poem, file=fout)
# fout.close()
#
# fout = open('relativity.txt', 'wt')
# print(poem, file=fout, sep='', end='')
# fout.close()
#
# fout = open('relativity.txt', 'wt')
# size = len(poem)
# offset = 0
# chunk = 100
# while True:
#     if offset > size:
#         break
#     print(fout.write(poem[offset:offset + chunk]))
#     offset += chunk
# fout.close()
#
# # fout = open('relativity.txt', 'xt') # FileExistsError: [Errno 17] File exists: 'relativity.txt'
# try:
#     fout = open('relativity.txt', 'xt')
#     fout.write('stomp stomp stomp')
# except FileExistsError:
#     print('relativity.txt already exists! That was a close one.')
#
# print()
#
# # 14.1.4 텍스트 파일 읽기: read(), readline(), readlines()
# fin = open('relativity.txt', 'rt')
# poem = fin.read()
# fin.close()
# print(len(poem))
#
# poem = ''
# fin = open('relativity.txt', 'rt')
# chunk = 100
# while True:
#     fragment = fin.read(chunk)
#     if not fragment:
#         break
#     poem += fragment
# fin.close()
# print(len(poem))
#
# poem = ''
# fin = open('relativity.txt', 'rt')
# while True:
#     line = fin.readline()
#     if not line:
#         break
#     poem += line
# fin.close()
# print(len(poem))
#
# poem = ''
# fin = open('relativity.txt', 'rt')
# for line in fin:
#     poem += line
# fin.close()
# print(len(poem))
#
# fin = open('relativity.txt', 'rt')
# lines = fin.readline()
# fin.close()
# print(len(lines), 'lines read')
# for line in lines:
#     print(line, end='')
#
# print()
#
# # 14.1.5 이진 파일 쓰기: write()
# bdata = bytes(range(0, 256))
# print(len(bdata))
#
# fout = open('bfile.txt', 'wb')
# print(fout.write(bdata))
# fout.close()
#
# fout = open('bfile.txt', 'wb')
# size = len(bdata)
# offset = 0
# chunk = 100
# while True:
#     if offset > size:
#         break
#     print(fout.write(bdata[offset:offset + chunk]))
#     offset += chunk
#
# print()
#
# # 14.1.6 이진 파일 읽: read()
# fin = open('bfile.txt', 'rb')
# bdata = fin.read()
# print(len(bdata))
# fin.close()
#
# print()
#
# # 14.1.7 자동으로 파일 닫기: with
# with open('relativity.txt', 'wt') as fout:
#     fout.write(poem)
#
# # 14.1.8 파일 위치 찾기: seek()
# fin = open('bfile.txt', 'rb')
# print(fin.tell())
#
# print(fin.seek(255))
#
# bdata = fin.read()
# print(len(bdata))
# print(bdata[0])
#
# import os
# print(os.SEEK_SET)
# print(os.SEEK_CUR)
# print(os.SEEK_END)
#
# fin = open('bfile.txt', 'rb')
#
# print(fin.seek(-1, 2))
# print(fin.tell())
#
# bdata = fin.read()
# print(len(bdata))
# print(bdata[0])
#
# fin = open('bfile.txt', 'rb')
#
# print(fin.seek(254, 0))
# print(fin.tell())
#
# print(fin.seek(1, 1))
# print(fin.tell())
#
# bdata = fin.read()
# print(len(bdata))
# print(bdata[0])
#
# print()
#
# # 14.2 메모리 매핑
#
# # 14.3 파일 명령어
#
# # 14.3.1 존재 여부 확인하기: exists()
# import os
# print(os.path.exists('oops.txt'))
# print(os.path.exists('./oops.txt'))
# print(os.path.exists('waffles'))
# print(os.path.exists('.'))
# print(os.path.exists('..'))
#
# print()
#
# # 14.3.2 유형 확인하기: isfile()
# name = 'oops.txt'
# print(os.path.isfile(name))
#
# print(os.path.isdir(name))
#
# print(os.path.isdir('.'))
#
# print(os.path.isabs(name))
# print(os.path.isabs('/big/fake/name'))
# print(os.path.isabs('big/fake/name/without/a/leading/slash'))
#
# print()
#
# # 14.3.3 복사하가ㅣ: copy()
# import shutil
# shutil.copy('oops.txt', 'ohno.txt')
#
# # 14.3.4 이름 바꾸기: rename()
# import os
# # os.rename('ohno.txt', 'ohwell.txt')
#
# # 14.3.5 연결하기: link() symlink()
# # os.link('oops.txt', 'yikes.txt')
# print(os.path.isfile('yikes.txt'))
#
# # os.symlink('oops.txt', 'jeepers.txt')
# print(os.path.islink('jeepers.txt'))
#
# print()
#
# # 14.3.6 권한 바꾸기: chmod()
# os.chmod('oops.txt', 0o400)
#
# import stat
# os.chmod('oops.txt', stat.S_IRUSR)
#
# # 14.3.7 소유권 바꾸기: chown()
# uid = 5
# gid = 22
# # os.chown('oops', uid, gid)
#
# # 14.3.8 파일 지우기: remove()
# os.remove('oops.txt')
# print(os.path.exists('oops.txt'))

### 권한 문제 발생 ###

# 14.4 디렉터리 명령어

# 14.4.1 생성하가: mkdir()
import os
os.mkdir('poems')
print(os.path.exists('poems'))

# 14.4.2 삭제하기 : rmdir()
os.rmdir('poems')
print(os.path.exists('poems'))

# 14.4.3 콘텐츠 나열하기: listidr()
os.mkdir('poems')

print(os.listdir('poems'))

os.mkdir('poems/mcintyre')
print(os.listdir('poems'))

fout = open('poems/mcintyre/the_good_man', 'wt')
print(fout.write('''Cheerful and happy wa his mod,
He to the poor was kind and good,
'''))
fout.close()

print(os.listdir('poems/mcintyre'))

print()

# 14.4.4 현재 디렉터리 위치 바꾸기: chdir()
import os
os.chdir('poems')
print(os.listdir('.'))

print()

# 14.4.5 일치하는 파일 나열하기: glob()
import glob
print(glob.glob('m*'))

print(glob.glob('??'))

print(glob.glob('m?????e'))

print(glob.glob('[klm]*e'))

print()

# 14.5 경로 이름
win_file = 'eek\\urk\\snort.txt'
win_file2 = r'eek\urk\snort.txt'
print(win_file)
print(win_file2)

print()

# 14.5.1 절대 경로 얻기: abspath()
print(os.path.abspath('oops.txt'))

print()

# 14.5.2 심볼릭 링크 경로 얻기: realpath()
print(os.path.relpath('jeepers.txt'))

# 14.5.3 경로 이름 작성하기: os.path.join()
import os
win_file = os.paht.join("eek", "urk")
win_file = os.path.join(win_file, "snort.txt")

# 14.5.4 pathlib 모듈
from pathlib import Path
file_path = Path('eek') / 'urk' / 'snort.txt'
print(file_path)
print(file_path)

print(file_path.name)
print(file_path.suffix)
print(file_path.stem)

# 14.6 BytesIO와 StringIO