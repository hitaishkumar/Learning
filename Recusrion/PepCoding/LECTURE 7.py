def power(a:int,p:int):
    if p == 1:
        return a
    return a * power(a,p-1)

print(power(3,3))