import Impfunc as im

a = im.createarray(20,1,20)
print(a)
ds = 18
ans = []
sum = 0
i = j = 0
a.sort()
print(" sorted --> " , a)
while j< len(a) -1 and i< len(a) - 1:
    if ds > sum:
        sum += a[j]
        # print(sum)
        ans.append(a[j])
        j+=1
    else:
        sum -= a[i]
        # print(sum)
        ans.remove(a[i])
        i+=1
    if ds == sum:
        print(" sum is found")
        print(ans)
        break
        
    