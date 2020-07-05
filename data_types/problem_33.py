"""
33. Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys
Sample Dictionary
"""
sample_dict = {}
for i in range(1, 16):
    sample_dict[i]=i*i
print(sample_dict)