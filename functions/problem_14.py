"""
14.Python program to sort a list of dictionaries using Lambda.
"""
def sort_list_dictionaries(sample_list):
    sample_list.sort(key=lambda x: x['model'])
    return sample_list
sample_list=[{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print(sort_list_dictionaries(sample_list))