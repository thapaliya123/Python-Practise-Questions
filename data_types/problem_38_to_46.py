"""
38. Write a Python program to remove a key from a dictionary.
"""
sample_dict = {1:2, 3:4, 5:6, 7:8}
delete_key = 1
del sample_dict[delete_key]
print(sample_dict)

"""
39. Write a Python program to unpack tuples in a several variables.
"""
sample_tuple = (1, 2, 3, 4, 5, 6)
for item in sample_tuple:
    print(item)

"""
40.Write a python program to add item in a tuple
"""
sample_tuple = (1, 2, 3, 4)
adding_item = 1
sample_list = list(sample_tuple)
sample_list.append(adding_item)
print(tuple(sample_list))
"""
41.Write a python program to convert tuple to string
"""
sample_tuple = (1, 2, 3, 4)
print("Tuple to string", str(sample_tuple))

"""
42.Write a python program to convert list to tuple
"""
sample_list = [1, 2, 3, 4]
print(f"List to tuple{tuple(sample_list)}")

"""
44.Write a python program to slice a tuple
"""
sample_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9)
start_index = 0
end_index = 4
interval = 1
print(f"The slice of tuple is: {sample_tuple[start_index:end_index:interval]}")

"""
45.Write a python program to find the index of an item in a tuple
"""
sample_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9)
for item in sample_tuple:
    print(f"The index of {item} is {sample_tuple.index(item)}")

"""
46.Write a python program to find the length of the tuple
"""
sample_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"The length of tuple {sample_tuple} is {len(sample_tuple)}")