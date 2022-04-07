str ="geeksforgeeks"

hashmap = {} 
hashmapp = {}
i = 0
for a in str:
    if a in hashmap:
        hashmap[a] += 1
    else:
        hashmap[a] = 1
print(hashmap)







