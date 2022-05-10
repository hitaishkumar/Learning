str ="geeksforgeeks"

hashmap = {} 
hashmapp = {}

for a in str:
    if a in hashmap:
        hashmap[a] += 1
    else:
        hashmap[a] = 1
print(hashmap)







