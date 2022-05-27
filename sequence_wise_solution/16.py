# find duplicate in an array of N+1 Integers

# Naive approach:

import random
ra= [ i+1 for i in range (10)]

ra.append(random.randint(1,10))

ra.sort()
# print(ra)




a = "_".join(str(i) for i in ra)

for i in range(len(ra)):
    if i+1 <= (len(ra)-1):
        if ra[i] == ra[i+1]:
            print(f"{ra[i] } is the duplicate in {ra} ")
            dup = ra[i]
            
with open("test.txt", "a") as myfile:
    myfile.write( "\n" + str(dup) + " is the duplicate in " +str(a) ) 