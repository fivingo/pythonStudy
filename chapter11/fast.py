from random import choice

places = ["McDonalds", "KFC", "Burger King", "Taco Bell", "Wendys", "Arbys", "Pizza Hut"]

def pick():
    """임의의 패스트푸드점을 반환한다."""
    return choice(places)