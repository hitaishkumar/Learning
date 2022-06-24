import Impfunc as imp

arr = imp.createarray(10,1,100) 
ans = []
d = 3
loop = len(arr) // d
i = 0
while i < (len(arr)):
    ans.append(arr[i:i+d])
    i += d
print(arr)
print(ans)
for i in ans[-1]:
    # print(i)
    for j in range(len(ans) - 2, 0, -1):
        if i  not in ans[j]:
            print(f" at index {j} , {i} is not present in {ans[j]}")
            break