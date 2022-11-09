'''power in log(n) time complexity'''
def power(x,n):
    if n == 0:
        return 1
    half_power = power(x,n//2)
    final_ans = power(half_power,2)
    if n % 2 == 1:
        final_ans = x * final_ans
    return final_ans
print(power(2,12))