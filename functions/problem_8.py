"""
8.Write a python function that takes a list and returns a new list with unique elements 
of the first list
"""

def return_unique_list_element(sample_list):
    return f"The list with unique element is:{list(set(sample_list))}"

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(return_unique_list_element(sample_list))