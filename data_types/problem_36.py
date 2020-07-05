"""
36. Write a Python program to sum all the items in a dictionary.
"""
sample_dict = {"1":2, "3":4, "5":6}
sum_items = 0
for key, value in sample_dict.items():
    print(value)
    sum_items = sum_items+value
print(f"The sum of the items in dictionary is:{sum_items}")