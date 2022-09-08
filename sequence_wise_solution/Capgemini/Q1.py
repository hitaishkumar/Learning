'''Removie duplicate from given array and find median of the array after sorting it out'''

a = [4,3,3,1,2]
b = [3,1,1,2]
a = list(set(a))
b = list(set(b))
a.extend(b)
a.sort()
print(a)

if len(a) %2 != 0:
    print(a[len(a)//2])
else:
    print(f"The median is {(a[(len(a)//2)-1] + a[(len(a)//2)])/2} Which is sum of {a[(len(a)//2)-1]} and {a[(len(a)//2)]}")