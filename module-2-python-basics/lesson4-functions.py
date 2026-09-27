# Lesson 4: Functions

# What is this topic?
# A function is a reusable block of code that performs a specific task.
# It helps us avoid repeating the same code.


# Key Vocabulary
#
# Function - a block of code that performs a specific task.
# def - a keyword used to create a function in Python.
# Parameter - a variable that receives a value inside a function.
# Argument - the actual value given to a parameter when calling a function.
# Return value - the value sent back by a function using return.
# Function call - using a function to run its code.


# My Own Example

def multiply(a, b):
    return a * b


result = multiply(4, 3)
print("Result:", result)


# Explanation:
# multiply is the function name.
# a and b are the parameters.
# 4 and 3 are the arguments.
# return sends the result back to the caller.
# multiply(4, 3) is the function call.
#
# Output:
# Result: 12


# A Mistake I Made
#
# One mistake I made was forgetting to give all the required arguments
# when calling a function.
#
# Example:
#
# multiply(4)
#
# This causes an error because the function needs two arguments,
# but I only provided one.
#
# I learned that I need to provide all the required arguments
# when calling a function.
