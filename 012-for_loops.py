l = [1, 2, 3, 4, 5]

for elements in l:
	print(elements)

print()

#MODULO

print("Modulo:")
print(10 % 3)
print(18 % 7)
print(4 % 2)

print()

for num in l:
	if num % 2 == 0:
		print(num)
	else:
		print("Odd number")

print()

list_sum = 0

for num in l:
	list_sum += num

print (list_sum)

print()

s = "this is a string"
for letter in s:
	print(letter)

print("\nTuples in for statment")

tup = (1, 2, 3, 4, 5)
for t in tup:
	print(t)

print("\nList Tuples in for loop")
l = [(2, 4), (6, 8), (10, 12)]
for item in l:
	print(item)

print("\nPrinting first value each item")
for (t1, t2) in l:
	print(t1)

print("\nDictionary in for loop")
d = {"k1": 1, "k2": 2, "k3": 3}
for item in d:
	print(item)

print("\nDictionary in for loop with .items()")
d = {"k1": 1, "k2": 2, "k3": 3}
for k, v in d.items():
	print(str(k) + ":" + str(v))


