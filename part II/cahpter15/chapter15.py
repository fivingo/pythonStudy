# CHAPTER 14 프로세스와 동시성

# 15.1 프로그램과 프로세스

import os

print(os.getpid())
print(os.getcwd())

print()

# 15.1.1 프로세스 생성하기(1): subprocess

import subprocess

# ret = subprocess.getoutput('date')
# print(ret)

# ret = subprocess.getoutput('date -u')
# print(ret)

# ret = subprocess.getoutput('date -u | wc')
# print(ret)

# ret = subprocess.getoutput('date', '-u')
# print(ret)

# ret = subprocess.getstatusoutput('date')
# print(ret)

# ret = subprocess.call('date')
# print(ret)

# ret = subprocess.call('date -u', shell=True)

# ret = subprocess.call('date', '-u')

# 15.1.4 시스템 정보보기: os
import os

# os.uname()
# os.uname()
# os.getloadavg()
print(os.cpu_count())

import os
# print(os.system('date -u'))

print()

# 15.1.5 프로세스 정보 보기: psutil

import psutil

print(psutil.cpu_times(True))

print(psutil.cpu_percent(True))
print(psutil.cpu_percent(percpu=True))

print()

# 15.2 명령 자동화

# 15.2.1 Invoke

