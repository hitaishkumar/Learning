'''Reverse an array'''

#  https://www.youtube.com/watch?v=twuC1F6gLI8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=4&ab_channel=takeUforward
import random
a =[]
for i in range(10):
    a.append(random.randint(2 , 100))
print(a ,  " --------> Generated array ")

def revarr(a ,l ,r):
    if l >= r:
        return
    a[l] , a[r] = a[r] , a[l]
    revarr(a, l + 1 , r - 1)
    return a
print(revarr(a, 0 , len(a) - 1) , " ------> reversed array")