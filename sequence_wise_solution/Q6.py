
# Q6/7 : Union & Intersection / Rotate Array || DSA Cracker Sheet || Complete Explanation || Code

# https://www.youtube.com/watch?v=ckqjEDwSqHM&ab_channel=DhruvGoyal

# FOR union


a = [1,32,5,4,6,4,8,12,6,4,8,1,2,4,1,65,1]
b = [1,4,54,4,1,6,1,5,1,5,1,58,1,21,4,8,1]

c = []
''' TIP: to add all element at once , USE "extend" like so, '''
c.extend(a)
c.extend(b)  
print(set(c))


# for intersection

''' For intersection(of sorted arrays) use two pointers with for most optimal methods'''
a.sort()
b.sort()
i = 0  # pointer at a[]
j = 0  # pointer at b[]
n = len(a)
m = len(b)
d = []

while (i<n and j< m):
    if a[i] < b[j]:
        i+=1
    elif a[i] > b[j]:
        j+= 1
    else:
        d.append(a[i])
        i+= 1
        j+= 1
print(d)
''' For intersection(of non sorted arrays) use HASH SET for most optimal methods'''