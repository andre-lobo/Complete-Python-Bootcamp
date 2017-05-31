# Errors and Exceptions Homework

# Problem 1: Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ["a", "b", "c"]:
        print(i ** 2)
except TypeError:
    print("There was a type error!")

print()


# Problem 2: Handle the exception thrown by the code below by using try and except blocks. 
# Then use a finally block to print "All Done."

try:
    x = 5
    y = 0

    z = x / y        
except:
    print("Can't divide by zero!")
finally:
    print("All done.")

print()


# Problem 3: Write a function that asks for an integer and prints the square of it. 
# Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    count_incorrect_inputs = 0

    while True:
        try:
            integer = int(input("Input an integer: "))
            result = integer ** 2
        except:
            print("An error ocurred! Please try again!")
            count_incorrect_inputs += 1
            continue
        else:
            print("Thank you, you number squared is: %s" %(str(result)))
            print("Incorrect Inputs: %s" %(count_incorrect_inputs))
            break

ask()