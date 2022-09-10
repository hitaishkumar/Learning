def findDisappearedNumbers(nums: list) -> list:
    
    
    ans = [i for i in range(1,len(nums)+1)]
    an = set(nums).symmetric_difference(set(ans))

    return an