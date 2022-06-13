# Subarray sum equals K | Number of subarrays with sum equals K | Leetcode #560
# https://www.youtube.com/watch?v=HbbYPQc-Oo4&ab_channel=TECHDOSE

from Impfunc import pav


k = 10
a =[6,-1,-3,4,-2,2,4,6,-12,-7]
prefix_sum = []
Curr_sum = 0
count = 0
map = {0:1}

for nums in a:
    Curr_sum += nums
    diff = Curr_sum - k
    
    count+= map.get(diff , 0)
    map[Curr_sum] = 1+ map.get(Curr_sum , 0)
pav()
print(count)
all_variables = dir()

# Iterate over the whole list where dir( )
# is stored.
for name in all_variables:

# Print the item if it doesn't start with '__'
    if not name.startswith('__'):
        myvalue = eval(name)
        print(name, "is", type(myvalue), "and is equal to ", myvalue)

















# for i in range(len(a)):
#     prefix_sum.append(Curr_sum + a[i]) 
#     if Curr_sum == k:
#         count+=1
#     if (map.get(Curr_sum - k,0) != 0):
#         count+= map.get(Curr_sum-k)
#     else:
#         if map.get(Curr_sum,0) == 0:
#             map[Curr_sum] = 1
#         else:
#             map[Curr_sum] += 1
# print(count)

