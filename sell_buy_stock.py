
prices = [7,1,5,3,6,4,56,23,45,78,45]
## Brute force
def maxprofit(x:list):
    profit = []
    for i in prices:
        for j in prices:
            if(j-i) >= 0:
                profit.append(j-i)
    # print(profit)
    return max(profit)
    
print(maxprofit(prices))