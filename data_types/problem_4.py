"""
Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
"""
first_string = 'anish'
second_string = 'manish'

combined_string = second_string[0:2]+first_string[2:]+" "+first_string[0:2]+second_string[2:]
print(combined_string)