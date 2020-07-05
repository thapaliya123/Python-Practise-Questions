"""
Q.Python program to get the largest number from a list.
"""

def find_largest_number(target_list):
    max = target_list[0]
    for item in target_list:
        if item>max:
            max = item
    return max
target_list = [1, 2, 3, 4, 5, 6]
print(f"The largest number in {target_list} is {find_largest_number(target_list)}")
