"""
18. Write a Python program to check whether a given string is number or not
using Lambda.
"""
check_numeric = lambda sample_string: "numeric" if sample_string.isnumeric()==True else "non-numeric"
sample_string = "204"
print(check_numeric(sample_string))
