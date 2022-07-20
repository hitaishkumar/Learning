import collections


a = "anagram"

b = "gramana"

c = collections.Counter(a)
d = collections.Counter(b)

print(c)
print(d)

print( c == d )

#  another solution is to sort the strings/number

a_sort = list(a).sort()
b_sort = list(b).sort()


print(a_sort == b_sort)