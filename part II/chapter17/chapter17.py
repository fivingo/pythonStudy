# CHAPTER 17 네트워크

# 17.1 TCP/IP

# 17.1.1 소켓

# 17.1.2 Scapy

# 17.1.3 Netcat

# 17.2 네트워크 패턴

# 17.3 요청-응답 패턴

# 17.3.1 ZeroMQ

# 17.3.2 기타 메시징 도구

# 17.4 발행-구독 패턴

# 17.4.1 Redis

# 17.4.2 ZeroMQ

# 17.4.3 기타 발행-구독 도구

# 17.5 인터넷 서비스

# 17.5.1 DNS

import socket
print(socket.gethostbyname('www.crappytaxidermy.com'))
print(socket.gethostbyname_ex('www.crappytaxidermy.com'))

print(socket.getaddrinfo('www.crappytaxidermy.com', 80))

print(socket.getaddrinfo('www.crappytaxidermy.com', 80, socket.AF_INET, socket.SOCK_STREAM))

import socket
print(socket.getservbyname('http'))
print(socket.getservbyport(80))

print()

# 17.5.2 파이썬 이메일 모듈

# 17.5.3 기타 프로토콜

# 17.6 웹 서비스와 API

# 17.7 데이터 직렬화

# 17.7.1 직렬화하기: pickle

import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now1)
print(now2)

import pickle
class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(obj1)
print(str(obj1))
pickled = pickle.dumps(obj1)
print(pickled)
obj2 = pickle.loads(pickled)
print(obj2)
print(str(obj2))

print()

# 17.7.2 기타 직렬화 형식

# 17.8 원격 프로시저 호출

# 17.8.1 XML PRC

# 17.8.2 JSON RPC

# 17.8.3 MessagePack RPC

# 17.8.4 Zerorpc

# 17.8.5 gRPC

# 17.8.6 Twirp

# 17.9 원격 관리 도구

# 17.10 빅데이터

# 17.10.1 하둡

# 17.10.2 스파크

# 17.10.3 디스코

# 17.10.4 데스크

# 17.11 클라우드

# 17.11.1 아마존 웹 서비스

# 17.11.2 구글 클라우드

# 17.11.3 마이크로소프트 애저

# 17.11.4 오픈스택

# 17.12 도커

# 17.12.1 쿠버네티스
