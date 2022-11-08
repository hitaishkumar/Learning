''' Factorials'''

def fact(a: int):
    if a == 0:
        return 1
    return a * fact(a-1)

print(fact(4))