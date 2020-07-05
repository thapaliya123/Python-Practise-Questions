"""
12. Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
"""

def multiply_with_unknown(sample_number):
    return lambda x:sample_number*x
sample_number=10
result = multiply_with_unknown(sample_number)
print(result(3))