"""
Q.Write a Python program to get the smallest number from a list.
"""

def find_smallest_number(target_list):
    small = target_list[0]
    for item in target_list:
        if item<small:
            small=item
    return small

target_list = [-1, 0, 1, 2]
print(f"smalles number in {target_list} is {find_smallest_number(target_list)}")