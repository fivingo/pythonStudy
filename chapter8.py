# CHAPTER 8 딕셔너리와 셋

# 8.1 딕셔너리

# 8.1.1 생성하기: {}
empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A perid of twenty-four hours, mostly miispent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)

print()

# 8.1.2 생성하기: dict()
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)
print()

# 8.1.3 변환하기: dict()
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))
