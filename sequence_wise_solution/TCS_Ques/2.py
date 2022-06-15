# Find the Largest element in an array

a = [int(input(f" enter the {i} element ")) for i in range(10)]

max = a[0]
for i in a:
    if i > max:
        max = i
print(max)