"""
15. Write a Python program to filter a list of integers using Lambda.
"""
sample_list = [1, 2, 3, 4, 5, 6]
sample_list = filter(lambda item:item%2==0,sample_list)
print(list(sample_list))