import random
class pair:
    def __init__(self) :
        self.max = 0
        self.min = 0

def get_min_max(arr: list,len: int) -> pair:
    
    minmax = pair()
    
    if len == 1:
        minmax.min = 0
        minmax.max = 0
        return minmax
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2,len):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        if arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax
a = random.choice([1, 4, 8, 10, 3,4,5,6,8,9,4,2,1,3])
b = [i**a for i in range(1,a)]
answer = get_min_max(b,len(b))
print(b)
print(answer.max)       
print(answer.min)       
