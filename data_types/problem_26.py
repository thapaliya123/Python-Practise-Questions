"""
26. Write a Python program to insert a given string at the beginning of all items in
a list.
"""

def insert_string_to_list_at_begining(sample_list, insert_string):
    string_to_list = [insert_string+str(item) for item in sample_list]
    return string_to_list
sample_list = [1, 2, 3, 4]
insert_string = "emp"
print(f"The list after insert {insert_string} at begining to list{sample_list} is {insert_string_to_list_at_begining(sample_list, insert_string)}")
