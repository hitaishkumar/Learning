import collections


a = "anagram"

b = "gramana"

c = collections.Counter(a)
d = collections.Counter(b)

print(c)
print(d)

print( c == d )