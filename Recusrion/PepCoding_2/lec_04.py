def factorial(a:int):
    if a <= 1:
        return 1
    return a * factorial(a-1)
new_var = factorial(5)
print(new_var)

'''iterative solution'''

def iterative_factorial(a:int):
    mult = 1
    for i in range(2,a+1):
        mult *= i
    return mult
print(iterative_factorial(5))