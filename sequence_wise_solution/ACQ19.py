# Find the maximum value and its index in the array
import Impfunc as im 

a = im.createarray(20,1,200)

max = a[0]
for i in range(len(a)):
    if a[i] >= max:
        max = a[i]
        index = i
print(f" Max is {max} at index {index} in {a} ")