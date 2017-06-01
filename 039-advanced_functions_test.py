# Advanced FUnctions Test

# Problem 1: Use map to create a function which finds the length of each word in the phrase 
# (broken by spaces) and return the values in a list.
# The function will have an input of a string, and output a list of integers.
# Output: [3, 4, 3, 3, 5, 2, 4, 6]

def word_lengths(phrase):
    return list(map(len, phrase.split()))

print(word_lengths('How long are the words in this phrase'))
print()


# Problem 2: Use reduce to take a list of digits and return the number that they correspond to. 
# Do not convert the integers to strings!
# Output: 34321
# Only in Python 2

def digits_to_num(digits):
    #return reduce(lambda x, y: x * 10 + y, digits)
    pass

print(digits_to_num([3,4,3,2,1]))
print()


# Problem 3: Use filter to return the words from a list of words which start with a target letter.
# Output: ['hello', 'ham', 'hi', 'heart']
def filter_words(word_list, letter):
    return list(filter(lambda word: word[0] == letter, word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']

print(filter_words(l,'h'))
print()


# Problem 4: Use zip and list comprehension to return a list of the same length where each value is 
# the two strings from L1 and L2 concatenated together with connector between them. Look at the 
# example output below:
# Output: ['A-a', 'B-b']

def concatenate(L1, L2, connector):
    return [word1 + connector + word2 for (word1, word2) in zip (L1, L2)]

print(concatenate(['A','B'],['a','b'],'-'))
print()


# Problem 5: Use enumerate and other skills to return a dictionary which has the values of the list 
# as keys and the index as the value. You may assume that a value will only appear once in the given list.
# Output: {'a': 0, 'b': 1, 'c': 2}

def d_list(L):
    return {key:value for value, key in enumerate(L)}

print(d_list(['a','b','c']))
print()


# Problem 6: Use enumerate and other skills from above to return the count of the number of items in the list 
# whose value equals its index.
# Output: 4

def count_match_index(L):
    return len([num for count, num in enumerate(L) if num == count])

print(count_match_index([0,2,2,1,5,5,6,10]))
print()