def findingUsersActiveMinutes(logs: list[list[int]], k: int):
    ul = []
    for i in range(0, len(logs)):
        ul.append(logs[i][0])
    ul = list(set(ul))
    hm = [[] for i in range(len(ul))]    
    for i in range(len(ul)):
        for j in range(1):
            if hm[logs[i][0]] in hm:
                hm[logs[i][0]].append(logs[i][1]) 
            else:
                hm[logs[i][0]] = [(logs[i][1])]   
    print(hm)
    
findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5)
   