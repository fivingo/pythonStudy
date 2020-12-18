# CHAPTER 12 데이터 길들이기

# 12.1 텍스트 문자열: 유니코드

# 12.1.1 파이썬 3 유니코드 문자열
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))
