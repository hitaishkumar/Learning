def getmazepath(SrSc:list, DrDc:list):
    # print(SrSc)
    # print(DrDc)
    if SrSc[0] > DrDc[0] or SrSc[1] > DrDc[1]:
        return []
    if SrSc[0] == DrDc[0] and SrSc[1] == DrDc[1]:
        return [""]
    rpath = [SrSc[0]+1,SrSc[1]]
    cpath = [SrSc[0],SrSc[1]+1]
    
    Rpath = getmazepath(rpath,DrDc)
    Cpath = getmazepath(cpath,DrDc)
    
    ans = ["V"+i for i in Rpath ]
    ans.extend(["H"+i for i in Cpath ])
    return ans
    
    
print(getmazepath([1,1],[3,2]))