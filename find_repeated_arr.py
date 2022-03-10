# Brute force solution without caring for time and space.
# a =[1,3,4,2,2]
# b = list(set(a))
# for i in b:
#     a.remove(i)
# print(a)
arr =[1,3,4,2,2]
def findduplicates(arr:list) -> list:
    output = []
    for i in range(len(arr)):
        index = arr[i] - 1  # becoz (array element <= array length)
        if arr[index] < 0 :
            output.append(index + 1)
        arr[index] = - arr[index]
    return output  

print(findduplicates(arr))
    

