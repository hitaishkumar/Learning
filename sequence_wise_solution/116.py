nums = [10, 3, 5, 6, 2]

prod = 1
for i in nums:
    prod *= i
ans = [str(prod// i) for i in nums]
print(" ".join(ans))
