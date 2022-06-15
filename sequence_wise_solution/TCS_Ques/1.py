# Find the smallest element in an array

a = [int(input(f" enter the {i} element ")) for i in range(10)]

min = a[0]

for i in a:
    if i < min:
        min = i
print(min)
