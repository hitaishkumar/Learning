arr = [1, 5, 7, 1]
givensum = 2
#brute force
def countpairs(arr: list,sum:int):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i != j:
                if arr[i]+arr[j] == sum:
                    print(f" number {arr[i]} and {arr[j]} at index {i} and {j} are answer")

# optimized solution using hash map
def countpairsoptimized(arr: list,sum:int):
    prevmap = {} # index: value
    for i,n in enumerate(arr): # i is index , n is number
        diff = sum - n
        if diff in prevmap:
            print(prevmap)
            
            return[prevmap[diff],i]
        prevmap[n] = i
    print(prevmap)
    return
print(countpairsoptimized(arr,2))     
    
    