from Impfunc import createarray

a =createarray(20,1,9)

#  TWO sum
a.sort()
print(a)
sum = 10        
ans = []

l , r = 0 , len(a)-1
print(r)
while l <= r:
    
    if (a[l]+ a[r]) > sum:
        r -= 1
    if (a[l]+ a[r]) < sum:
        l += 1
    if (a[l]+ a[r]) == sum:
        ans.append(a[l])
        ans.append(a[r])
        break
print(ans)