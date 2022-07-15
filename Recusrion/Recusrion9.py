''' Subsequence || power set '''



def subsequence(a : list):
    if len(a) == 0:
        return [" "]
    
    small = subsequence(a[1:len(a)])

    result =  [" "] * (2 * len(small))
    k = 0
    
    for i in range(len(small)):
        result[k] = small[i]
        k+= 1
    
    for i in range(len(small)):
        result[k] = a[0] + small[i]
        k+= 1
    return result

arr = ["c" , "d" , "e" , "f" ]
arr_num = [ "1" , "2" , "3" ]

print(subsequence(arr))
print(subsequence(arr_num))