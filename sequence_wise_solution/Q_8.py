#  Q8 : Find Largest sum contiguous Subarray || DSA Cracker Sheet || Complete Explanation || Code

#  https://www.youtube.com/watch?v=qrmcjKzNW-Q&list=PL1pnzsTb-IKhg7TzdoIYYzIyGhzRzeH0t&index=7&ab_channel=DhruvGoyal

# kadanes's algorithm


import random
ra= []
for i in range(50):
   ra.append(random.randint(-100,-10)) 
print(ra)
print(len(ra))

currsumm = 0
maxsum = ra[0]
ans = []
for i in ra:
    if currsumm < 0:
        currsumm = 0
        ans = []
    currsumm += i
    ans.append(i)
    maxsum = max(currsumm,maxsum)

print(f' the max sum subarray is {ans} and the sum is {maxsum} ')