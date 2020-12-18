# 11.1.1 모듈 임포트하기

places = ["McDonals", "KFC", "Burger King", "Taco Bell", "Wendys", "Arbys", "Pizza Hut"]

def pick():
    import random
    return random.choice(places)
