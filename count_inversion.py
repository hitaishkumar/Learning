import timeit

sts = '''factorial function''' 
def fac(x:int):
    if x == 0:
        return 1
    answer = x * fac(x-1)
    return answer
# print(fac(0))

arr = [2, 3, 4, 5, 6]
starttime = timeit.default_timer()
print("The start time is :",starttime)
print(fac(899)) # The time difference is : 0.004297499996027909
    # without print // The time difference is : 0.004297499996027909
print("The time difference is :", timeit.default_timer() - starttime)