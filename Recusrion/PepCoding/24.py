a = [8,4,5,6,4]

def findallindices(array,idx,findnum):
    
    if idx == len(array): return []
    
    aiisa = findallindices(array,idx+1,findnum)
    
    if array[idx] == findnum: 
        aiisa.insert(0,idx)
        return aiisa
    else:
        return aiisa
    
     
    
print(findallindices(a,0,4))