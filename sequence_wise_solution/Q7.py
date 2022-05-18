<<<<<<< HEAD
# Q6/7 : Union & Intersection / Rotate Array || DSA Cracker Sheet || Complete Explanation || Code

# https://www.youtube.com/watch?v=ckqjEDwSqHM&ab_channel=DhruvGoyal


''' Rotate a array by RIGHT or LEFT '''



a = [1,32,5,4,6,4,8,12,6,4,8,1,2,4,1,65]

temp = a[len(a)-1]  
i = len(a) - 1
while(i-1 >= 0):
    a[i] = a[i-1]
    i-=1
a[0] = temp
print(a)

=======
# Q6/7 : Union & Intersection / Rotate Array || DSA Cracker Sheet || Complete Explanation || Code

# https://www.youtube.com/watch?v=ckqjEDwSqHM&ab_channel=DhruvGoyal


''' Rotate a array by RIGHT or LEFT '''



a = [1,32,5,4,6,4,8,12,6,4,8,1,2,4,1,65]

temp = a[len(a)-1]  
i = len(a) - 1
while(i-1 >= 0):
    a[i] = a[i-1]
    i-=1
a[0] = temp
print(a)

>>>>>>> 0029884205f0610e428535119c7119e8a4749243
''' ans = [65, 1, 32, 5, 4, 6, 4, 8, 12, 6, 4, 8, 1, 2, 4, 1]'''