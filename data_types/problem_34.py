"""
34.Write a Python script to merge two Python dictionaries.
"""
sample_dict1 = {1:2, 3:4, 5:6}
sample_dict2 = {7:8, 9:10, 11:12}
merged_dict = {}
merged_dict.update(sample_dict1)
merged_dict.update(sample_dict2)
print("The new dictionary after merging the two dictionary is:", merged_dict)