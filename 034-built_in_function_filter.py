# Build-in function: Filter

def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(even_check(35))
print()

lst = list(range(10))

print(list(filter(even_check, lst)))

print(list(filter(lambda num: num % 2 == 0, lst)))

print(list(filter(lambda num: num > 3, lst)))