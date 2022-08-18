n = int(input())
a = []
c =  0
digits = []
for i in range(0,n):
    # print("eojrting")
    digits.clear()
    digits = [x for x in str(i)]
    # print(digits)
    if '9' in digits:
        a.append(i)
# print(a)

def solve(a: list, n: int, sum: int):
    tab = [[0] * (sum + 1) for i in range(n + 1)]
    tab[0][0] = 1
    for i in range(1, sum + 1):
        tab[0][i] = 0
     
    for i in range(1, n+1):
        for j in range(sum + 1):
            if a[i-1] <= j:
                tab[i][j] = tab[i-1][j] + tab[i-1][j-a[i-1]]
            else:
                tab[i][j] = tab[i-1][j]
    return tab[n][sum]

if n < 9 and n > 0:
    print('0')
elif n == 9:
    print('1')
else:
    print(solve(a,len(a),n))
