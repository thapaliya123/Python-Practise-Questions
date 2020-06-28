"""
16. Write a Python program to square and cube every number in a given list of
integers using Lambda.
"""
sample_list = [1, 2, 3, 4]
square_cube = map(lambda item:(item**2, item**3),sample_list)
print(list(square_cube))