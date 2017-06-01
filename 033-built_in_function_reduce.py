# Build-in function: Reduce 
# Not exist in Python 3

lst = [34, 23, 24, 24, 100, 2333, 2, 11]

result = max(lst)

max_find = lambda a, b: a if (a > b) else b

#reduce(max_find, list)

def max_find(a, b):
    if a > b:
        return a
    else:
        return b

print(max_find(12, 100))