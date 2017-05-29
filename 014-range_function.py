#range function examples

x = list(range(0, 10))

print(type(x))
print(x)

start = 0
stop = 20

x = list(range(start, stop, 3))
print(x)

print()

#save in the memory in python 2.
#in python 3 not save in memory.
#in python 2 is recomended uses xrange for gigant numbers
for num in range(1, 6):
	print(num)

print()