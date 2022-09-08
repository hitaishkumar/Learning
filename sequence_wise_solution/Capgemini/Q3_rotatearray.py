''' Rotate an array'''

a = [1,2,3,4,5,6,7,8,9,10]

# rotate Left
l = 6
ans = a[l:]
ans.extend(a[:l])

print(ans)
# rotate Right
r = 3
ans = a[len(a)-r:]
ans.extend(a[:len(a) - r])
print(ans) 