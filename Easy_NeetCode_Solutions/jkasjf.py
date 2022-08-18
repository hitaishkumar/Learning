# a = [1, 7 , 4 ,6]
# a =[1 , 2 , 3 , 4, 5]
a = [3,3,5,3,6]

def maxProfit(a):
    profit  = 0
    c = len(a)
    
    if len(a) == 0:
        return 0

    while c > 2:
        c_i = len(a) - 2
        profit += min(a[c_i - 1], a[c_i + 1])
        a.pop(c_i)
        c -= 1    
    
    return profit
print(maxProfit(a))