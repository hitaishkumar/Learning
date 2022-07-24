import collections


a = ['a' , 'b', 'b' , 'd' , 'e' , 'f']
count = 0
print(collections.Counter(a))
if len(a) == 1:
    print("1")
b = set(a)
if len(b) == len(a):
    print(len(a))
elif len(a) > 2:
    for b in b :
        a.remove(b)
        count += 1
    
    for i in range(1,len(a)):
        
        if a [i] != a[i-1]:
            count += 2
    print(count, "fhfgh")