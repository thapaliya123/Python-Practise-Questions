"""
37. Write a Python program to multiply all the items in a dictionary.
"""
sample_dict = {1:2, 3:4, 5:6, 7:8}
mul = 1
for value in sample_dict.values():
    mul = mul*value

print(mul)