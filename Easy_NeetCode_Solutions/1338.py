
'''

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
'''

import collections


arr = [3,3,3,3,5,5,5,2,2,7]
freq = []
aset = set(arr)
for a in aset:
    freq.append(arr.count(a))
# counter = collections.Counter(arr)
# print(counter)
freq.sort()
print(freq)