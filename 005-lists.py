#lists examples

my_list = [1, 2, 3]

my_another_list = ["text", 23, 1.3, "A"]

print(len(my_list))
print(len(my_another_list))

my_another_list = ["One", "Two", "Three", 4, 5]
print(my_another_list[0])
print(my_another_list[1:])
print(my_another_list[:3])

print("\n Add new item in list")

#add new item in list
my_list = my_list + [4]
my_another_list = my_another_list + ["Five"]

print(my_list)
print(my_another_list)

print(my_list * 2)

print("\n Append")

#append
l = [1, 2, 3]
l.append("append me")
print(l)

print(l.pop())
print(l)

x = l.pop(0)
print(x)
print(l)

print("\n Sort")

#sort
new_list = ["a", "e", "x", "b", "c"]
new_list.reverse()
print(new_list)

new_list.sort()
print(new_list)

new_list.sort(reverse = True)
print(new_list)

print("\n Matrix")

#matrix
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]

matrix = [l_1, l_2, l_3]
print(matrix)

print(matrix[0])
print(matrix[0][2])

first_col = [row[0] for row in matrix]
print(first_col)