"""
25. Write a Python program to check whether all dictionaries in a list are empty or
not.
"""
list_with_dict = [{1:2, 3:4}, {}, {}]
count = 0
for item in list_with_dict:
    if len(item)==0:
        count=count+1
if count==len(list_with_dict):
    print(True)
else:
    print(False)