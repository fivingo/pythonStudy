# CHAPTER 18 웹

# 18.1 웹 클라이언트

# 18.1.1 telnet으로 테스트하기

# 18.1.2 curl로 테스트하기

# 18.1.3 httpie로 테스트하기

# 18.1.4 httpbin으로 테스트하기

# 18.1.5 파이썬 표준 웹 라이브러리

import urllib.request as ur
import webbrowser

url = 'http://www.example.com/'
conn = ur.urlopen(url)

print(conn.status)

data = conn.read()
print(data[:50])

str_data = data.decode('utf-8')
print(str_data[:50])

for key, value in conn.getheaders():
    print(key, value)

print()

# 18.1.6 표준 라이브러리를 너머서: requests

import requests
resp = requests.get('http://example.com')
print(resp)
print(resp.status_code)
print(resp.text[:50])

print()

# 18.2 웹 서버

# 18.2.1 간단한 파이썬 웹 서버

# 18.2.2 웹 서버 게이트웨이 인터페이스

# 18.2.3 ASGI

# 18.2.4 아파치

# 18.2.5 엔진엑스

# 18.2.6 기타 파이썬 웹 서버

# 18.3. 웹 서버 프레임워크

# 18.3.1 Bottle

# 18.3.2 Flask

# 18.3.3 장고

# 18.3.4 기타 프레임워크

# 18.4 데이터베이스 프레임워크

# 18.5 웹 서비스와 자동화

# 18.5.1 webbrowser 모듈

import antigravity
url = 'http://www.python.org/'
# print(webbrowser.open(url))

# print(webbrowser.open_new(url))

# print(webbrowser.open_new_tab(url))

# 18.5.2 webview 모듈

# 18.6 웹 API와 REST

# 18.7 크롤링과 스크래핑

# 18.7.1 Scrapy

# 18.7.2 BeauifulSoup

# 18.7.3 Requests-HTML

# 18.8 영화 검색 예제