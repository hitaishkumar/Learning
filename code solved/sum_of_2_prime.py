
a = 74
def isprime(n:int):
    for i in range(2,n):
        if (n%i) == 0:
            # break   
            return False
       
    return True
# print(isprime(a))
for i in range(2,a):
    if (isprime(i)):
        if (isprime(a-i)):
            print(f" yes, its sum of {i} and {a-i}")