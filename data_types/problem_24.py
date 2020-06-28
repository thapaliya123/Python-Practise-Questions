"""
24. Write a Python program to clone or copy a list.
"""
def clone_list(target_list):
    copy_list = target_list[:]
    return copy_list

target_list = [1, 2, 3, 4, 5]
print(f"The resulting list after cloning is: {clone_list(target_list)}")