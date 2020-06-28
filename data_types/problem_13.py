"""
Q.Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
"""

comma_separate_word = input("enter any sentence word separated by comma")
words = comma_separate_word.split(",")
print(sorted(list(set(words))))