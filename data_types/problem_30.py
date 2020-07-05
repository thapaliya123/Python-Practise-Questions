"""
30. Write a Python script to check whether a given key already exists in a
dictionary.
"""
sample_dict = {1:2, 3:4, "anish":6}
check_key = 4
if check_key in sample_dict.keys():
    print(True)

else:
    print(False)
