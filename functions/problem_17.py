"""
17.Write a Python program to find if a given string starts with a given character
using Lambda.
"""
string_with_given_char = lambda sample_string, sample_char: True if sample_string[0]==sample_char else False
sample_string="anish"
sample_char = "a"
print(string_with_given_char(sample_string, sample_char))