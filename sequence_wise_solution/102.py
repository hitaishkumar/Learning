# Find equilibrium point in an array
#  https://www.youtube.com/watch?v=c9imv2LvgWk&ab_channel=TECHDOSE

# import Impfunc as im
# a = im.createarray(10,2,10)
a = [7, 2, 10, 7, 3, 2, 4, 10, 5, 10]


'''Brute force metheod O(n^2)'''
# print(a)
# for i in range(1,len(a)):
#     left_sum = sum(a[0:i])
#     right_sum = sum(a[i+1:len(a)])
   
    
#     if left_sum == right_sum:
#         print(i)
        
'''optimal method'''

sum_arr = []
sum = 0
for i in range(len(a)):
    sum += a[i]
    sum_arr.append(sum)
print(sum_arr) # [7, 9, 19, 26, 29, 31, 35, 45, 50, 60]

for i in range(1,len(sum_arr)):
     left_sum = sum_arr[i] - a[i]
     right_sum = sum_arr[-1] - sum_arr[i]
     
     if left_sum == right_sum:
         print(f" index is {i} and num is {a[i]} ")
    