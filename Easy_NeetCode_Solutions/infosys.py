


a = [1,7,4,6]
# n = int(input())
# for i in range(n):
#     a.append(int(input()))
# print(a)
profit  = 0
while len(a) > 0:
    if len(a)== 1:
        profit += a[0]
        a.remove(a[0])
    if len(a) == 3:
        if a[0] >= a[2]:
            profit += a[2]
            a.remove(a[2])
        else:
            profit += a[0]
            a.remove(a[0])
    
    if a[len(a) - 1] > a[len(a)-3]:
        profit += a[len(a) - 3]
        a.remove(a[len(a) - 3])
    else:
        profit += a[len(a) - 1]
        a.remove(a[len(a) - 1])
        
    