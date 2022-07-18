def placement(input1,input2):

    ''' Placement season begins'''
    ans = []
    ans.append(0)
    count = 0
    for i in range(1,len(input2)):
        for j in input2[0:i]:
            if j > input2[i]:
                count += 1
        
        ans.append(int(count))
        count = 0
    return ans
        
# print(placement(6,[4,9, 5,3,2,10]))  
# print(placement(5,[3,4,1,5,2]))  
