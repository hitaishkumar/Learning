m = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15,16]]

rowbegin = 0
rowend = len(m)
colbegin = 0
colend = len(m[0])

output = []

while(rowbegin < rowend and colbegin < colend):
    
    for i in range(colbegin,colend):
        print(m[rowbegin][i])
        output.append(m[rowbegin][i])
    for j in range(rowbegin,rowend):
        print(m[j][colend-1])
        output.append(m[j][colend-1])
    if rowend != rowbegin +1:
        for i in range(colend-1, colbegin -1,-1):
            print(m[rowend -1][i])
            output.append(m[rowend -1][i])
    if colbegin!= colend - 1:
        for j in range(rowend - 2,rowbegin ,-1):
            print(m[j][colbegin])
            output.append(m[j][colbegin])           
    rowbegin +=1
    rowend -= 1
    colbegin +=1
    colend -= 1
print(output)