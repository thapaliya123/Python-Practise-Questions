"""
Q.Python program to change a given string to a new string where the first
and last chars have been exchanged.
"""

sample_string = input("enter any word\n")
string_change_first_last_char = sample_string[-1]+sample_string[1:len(sample_string)-1]+sample_string[0]
print(string_change_first_last_char)