def main():
	a = [(i+4) for i in range(48)]
	print(a) # [4, 5, 6, 7, 8]
	
	start = 0
	end = len(a) - 1
	x = 0
	while start < end:
		x = a[start]
		a[start] = a[end]
		a[end] = x
		start += 1
		end -= 1
		# print(" cycle no  " + str(start) + " has the array  "+ str(a) )
	print(a)
