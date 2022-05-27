#  https://www.youtube.com/watch?v=1S4KFg5viC0&ab_channel=OhMyCode%21

# Merge Two Sorted Arrays Without Using Extra Space(Hindi) || Merge with O(1) space


import random
ra= []
for i in range(10):
    ra.append(random.randint(-5,5))
    
outt = []
def kadane(ra:list):
    max_curr = max_global = ra[0]
    for i in range (1,len(ra)):
        if  ra[i] < max_curr + ra[i]:
            outt.append(ra[i]) # not accurate
        max_curr = max(ra[i] , max_curr + ra[i])
        
    print(outt) # [print the ele that are summed]
    
    if max_curr > max_global:
        max_global = max_curr
    
    return max_global
print(ra)
print(kadane(ra))
