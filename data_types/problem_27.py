"""
27. Write a Python program to replace the last element in a list with another list.
"""
sample_list_one = [1, 3, 5, 6]
sample_list_two = [7, 8, 9, 10]

list_after_replace_last_element = sample_list_one[0:-1]+sample_list_two
print(list_after_replace_last_element)