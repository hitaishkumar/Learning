''' Alice guessing game'''
import random
ra= []
for i in range(10):
    ra.append(random.randint(10,15))

print(ra)

# print(ra[-1])
# ir = input('Alice guessing game').split()
# print(ir)

if ra[-1] == ra[0]:
    print(" hurray everyone gets prize")
else:
    print(ra.count(ra[0])-1)