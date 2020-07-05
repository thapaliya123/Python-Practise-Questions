"""
10.Write a python program to print the even numbers from a given list
"""

def return_even_number_list(sample_list):
    even_list = [item for item in sample_list if item%2==0]
    return even_list
sample_list = [1, 2, 3, 4, 5, 6]
print(return_even_number_list(sample_list))