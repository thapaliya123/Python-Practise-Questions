"""
Q.Write a Python program to multiplies all the items in a list.
"""
from functools import reduce
target_list = [1, 2, 3, 5]
val = reduce(lambda x,y:x*y, target_list)
print(f"multiplication of all the list items{target_list} is: *{val}*")
