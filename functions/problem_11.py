"""
11. Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
"""
add_number_15 = lambda number: number+15
print(add_number_15(10))

multply_two_argument = lambda x,y:x*y
print(multply_two_argument(10, 20))