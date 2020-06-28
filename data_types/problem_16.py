"""
Q.a Python program to sum all the items in a list.
"""
def sum_list_items(target_list):
    sum=0
    for item in target_list:
        sum+=item
    return sum

print("The sum of list is:", sum_list_items([1, 2, 3, 4, 5]))