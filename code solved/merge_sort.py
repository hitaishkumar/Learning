# time complexity of merge sort is O(nlogn
# General Principle
'''
Merge Sort:
1.Split array in half
2.Call Merge Sort on each half to sort them recursively

3.Merge both sorted halves into one sorted array

'''




def mergesort(arr:list) -> list:
    if len(arr) > 1 :
        left_arr = arr[:(len(arr)//2)] # returns slice of array on the array on left
        right_arr = arr[len(arr)//2:] # returns slice of array on the array on right
        
        # recursively sort the divided arraay
        mergesort(left_arr)
        mergesort(right_arr)
        
        i = 0 #left arr index
        j = 0 #right arr index
        k = 0 #merge arr index


        # merge
        while(i < len(left_arr) and j < len(right_arr)):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i +=1
            else:
                arr[k] = right_arr[j]
                j += 1
            k +=1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i +=1
            k += 1    
        while j < len(right_arr):
            arr[k] = left_arr[j]
            j +=1
            k +=1    