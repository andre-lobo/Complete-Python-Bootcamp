#list comprehensions

l = []

for letter in "word":
	l.append(letter)

print(l)
print()

l = [letter for letter in "Word"]
print(l)
print()

lst = [x ** 2 for x in range(1, 11)]
print(lst)

lst = [number for number in range(11) if number % 2 == 0]
print(lst)

lst = []
for number in range(11):
	if number % 2 == 0:
		lst.append(number)

print(lst)
print()

celsiu = [0, 10, 20.1, 34.5]
fahrenheit = [ (temp * (9/5) + 32) for temp in celsiu]
print(celsiu)
print(fahrenheit)
print()

#final result is x ** 4 for num in range(11)
lst = [x ** 2 for x in [x ** 2 for x in range(11)]]
print(lst)