
def fac(x:int):
    if x == 0:
        return 1
    answer = x * fac(x-1)
    return answer
# print(fac(0))

arr = [2, 3, 4, 5, 6]
