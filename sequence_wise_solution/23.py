import Impfunc

a = Impfunc.createarray(10,1,10)
sum = 5
print(a)
for i in a:
    if sum - i in a:
        print(f"{sum} is sum of {i} and {sum - i} ")
