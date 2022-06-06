import Impfunc as im
''' Finding max of an array using resursion '''
a = im.createarray(10,1,8)
def findmaxrecur(array:list,index:int):
    if index == len(array) - 1:
        return array[index]
    max_of_small_array = findmaxrecur(array,index+1)
    
    if max_of_small_array > array[index]:
        return max_of_small_array
    else:
        return array[index]
print(a)
findmaxrecur(a,0)
    