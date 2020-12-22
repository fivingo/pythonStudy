# CHAPTER 13 날짜와 시간

# 13.1 윤년
import calendar
print(calendar.isleap(1900))
print(calendar.isleap(1996))
print(calendar.isleap(1999))
print(calendar.isleap(2000))
print(calendar.isleap(2002))
print(calendar.isleap(2004))

print()

# 13.2 datetime 모듈
from datetime import date
halloween = date(2019, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)

print(halloween.isoformat())

now = date.today()
print(now)

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
print(now + 17 * one_day)
yesterday = now - one_day
print(yesterday)

from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

from datetime import datetime
some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
print(some_day)

print(some_day.isoformat())

from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)

print(noon_today.date())
print(noon_today.time())

print()

# 13.3 time 모듈
import time
now = time.time()
print(now)

print(time.ctime(now))

print(time.localtime(now))
print(time.gmtime(now))

import time
now = time.localtime()
print(now)
print(now[0])
print(list(now[x] for x in range(9)))

# tm = time.localtime(now)
# print(time.mktime(tm))

print()

# 13.4 날자와 시간 읽고 쓰기
import time
now = time.time()
print(time.ctime(now))

fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
print(time.strftime(fmt, t))

from datetime import date
some_day = date(2019, 7, 4)
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
print(some_day.strftime(fmt))

from datetime import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
some_time = time(10, 35)
print(some_time.strftime(fmt))

import time
fmt = "%Y-%m-%d"
# print(time.strptime("2019 01 29", fmt)) # ValueError: time data '2019 01 29' does not match format '%Y-%m-%d'

fmt = "%Y-%m-%d"
print(time.strptime("2019-01-29", fmt))

fmt = "%Y %m %d"
print(time.strptime("2019 01 29", fmt))

fmt = "%Y-%m-%d"
# print(time.strptime("2019-13-29", fmt)) # ValueError: time data '2019-13-29' does not match format '%Y-%m-%d'

import locale
from datetime import date
halloween = date(2019, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime('%A, %B %d')

names = locale.locale_alias.keys()

good_names = [name for name in names if \
              len(name) == 5 and name[2] == '_']

print(good_names[:5])

de = [name for name in good_names if name.startswith('de')]
print(de)
