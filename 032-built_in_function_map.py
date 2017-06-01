# Build-in function: Map

def fahrenheit(T):
    return  (9/5) * T + 32

print("0")

temp = [0, 22.5, 40, 100]

result = map(fahrenheit, temp)
print(list(result))

result = map(lambda T: (9/5) * T + 32, temp)
print(list(result))

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

result = map(lambda x, y, z: x + y + z, a, b, c)
print(list(result))

result = map(lambda num: num * -1, a)
print(list(result))