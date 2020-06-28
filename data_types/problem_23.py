"""
23. Write a Python program to check a list is empty or not.
"""
def check_empty_list(target_list):
    if(len(target_list)>0):
        return "List is not empty"
    
    else:
        return "List is empty"

target_list = [1, 2]
print(check_empty_list(target_list))