"""
13. Write a Python program to sort a list of tuples using Lambda.
"""
def sort_list_tuple(sample_list):
    sample_list.sort(key = lambda x: x[1])
    return sample_list
sample_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sort_list_tuple(sample_list))