import random

a = [random.randint(1, 20) for i in range(50)]
# print (a)

# target = 5

# a.sort()
# # print (a)
# b = a
# start = 0
# end = len(b) - 1
# sum = 0
# while(start< end):
#     sum = b[start] + b[end]
#     if sum < target:
#         start += 1
#     else:
#         end -= 1
        
        
#     if  sum == target:
#         print(f" {b[start]} at index {start}, {b[end]} at index  {end}, have a sum of {sum}")
#         break
b = [3,2,4]
def twoSum( nums, target) :
        a = [i for i in nums]
        
        nums.sort()
        print(a)
        i , j = 0 , len(nums)-1
        if len(nums) >1:
        
            while (i<j):
                if nums[i] + nums[j] == target:
                    return [a.index(nums[i]) , a.index(nums[j])]
                    
                elif nums[i] + nums[j] <= target:
                    i += 1
                elif nums[i] + nums[j] >= target:
                    j -= 1
print(twoSum(b,6))