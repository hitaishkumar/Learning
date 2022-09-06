def isHappy(n: int) -> bool:
        s  = set()
        # sum = 0
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            print([int(i)**2 for i in str(n)] ,' sums upto  ' , n)
            if n in s:
                return False
            else:
                s.add(sum)
        return True
print(isHappy(23))