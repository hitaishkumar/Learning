# https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/

'''

Given a binary string str of length N,
the task is to find the maximum count of consecutive substrings
str can be divided into such that all the substrings are balanced i.e.
they have equal number of 0s and 1s. 
If it is not possible to split str satisfying the conditions then print -1.
'''

# str = "0100110101"
str = "0111100010"
co = 0
ci = 0 
ans = 0
for i in str:
    i = int(i)
    if i == 0:
        co +=1
    else: 
        ci += 1
    if co == ci:
        ans+= 1
        co = ci = 0
    if not ans:
        print(-1)
print(ans)
        