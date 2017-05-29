# functions and methods homework

import math
import string

# 1. Write a function that computes the volume of a sphere given its radius.
print("*** Resolution of Exercise 1 ***")

def vol(rad):
    return (4 * math.pi * (rad ** 3)) / 3

print(vol(5))


# 2. Write a function that checks whether a number is in a given range
# (inclusive of high and low).
print("\n*** Resolution of Exercise 2 ***")

def ran_check(num, low, high):
    if num in range(low, high):
        print("%s is in the range" % str(num))
    else:
        print("The number is outside the range")

def ran_boolean_v1(num, low, high):
    lst = list(range(low, high))
    return lst.count(num) > 0

def ran_boolean_v2(num, low, high):
    return num in range(low, high)

ran_check(5, 1, 20)
print(ran_boolean_v1(5, 1, 20))
print(ran_boolean_v2(5, 1, 20))


# 3. Write a Python function that accepts a string and calculate the
# number of upper case letters and lower case letters.
print("\n*** Resolution of Exercise 3 ***")

# Sample String: Hello Mr. Rogers, how are you this fine Tuesday?
# Expected Output:
# No. of Upper case characters: 4
# No. of Lower case characters: 33

def up_low_my_version(s):
    upper = 0
    lower = 0

    for letter in s:
        if letter.isupper():
            upper += 1

        if letter.islower():
            lower += 1

    return "No. of Upper case characters: {u}\nNo. of Lower case characters: {l}".format(u=upper, l=lower)

def up_low_course_version(s):
    d = {"upper": 0, "lower": 0}

    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass

    return "\nNo. of Upper case characters: {u}\nNo. of Lower case characters: {l}".format(u=d["upper"], l=d["lower"])

print(up_low_my_version("Hello Mr. Rogers, how are you this fine Tuesday?"))
print(up_low_course_version("Hello Mr. Rogers, how are you this fine Tuesday?"))


# 4. Write a Python function that takes a list and returns a new list with
# unique elements of the first list.
print("\n*** Resolution of Exercise 4 ***")

# Sample List: [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
# Unique List: [1, 2, 3, 4, 5]

def unique_list_my_version(l):
    return list(set(l))

def unique_list_course_version(l):
    x = []

    for a in l:
        if a not in x:
            x.append(a)

    return x

print(unique_list_my_version([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
print(unique_list_course_version([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# 5. Write a Python function to multiply all the numbers in a list.
print("\n*** Resolution of Exercise 5 ***")

# Sample List: [1, 2, 3, -4]
# Expected Output: -24

def multiply(numbers):
    result = numbers[0]

    for n in numbers:
        result *= n

    return result

print(multiply([1, 2, 3, -4]))


# 6. Write a Python function that checks whether a passed string is
# palindrome or not.
print("\n*** Resolution of Exercise 6 ***")

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward
# e.g.: madam, nurses run

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("nurses run"))
print(is_palindrome("andre"))


# 7. Write a Python function to check whether a string is pangram or not.or
print("\n*** Resolution of Exercise 7 ***")

# Note: Pangrams are words or sentences containing every letter of the alphabet at least once.letter
# e.g.: "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module

def is_pangram(str1, alphabet=string.ascii_lowercase):
    alpraset = set(alphabet)
    return alpraset <= set(str1.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("My name is Andre"))

#string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'