#  Find whether an array is a subset of another array | Q27 | DSA Sheet | Leetcode | GFG | Qualcomm
# Approach 1
import Impfunc as im

big  = im.createarray(10,1,10)
small  = im.createarray(5,1,5)

def subarray(big:list , small: list):  # TC : O(N^2) 
    for i in small :
        if i not in big :
            return False
    return True




# Optimal approach

def subarrayy(big:list , small: list) -> bool:
    # convert List to Dict with desired value
    big_dict = dict.fromkeys(big,1)
    print(big_dict)
    for i in small:
        if big_dict.get(i,"0") == "0":
            return False
    return True
# print(big)
# print(small)
print(subarrayy(big,small))