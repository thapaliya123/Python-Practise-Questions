"""
Q.Python function that takes a list of words and returns the length of the
longest one.
"""

def return_longest_word(list_of_words):
    longest_length = 0
    for word in list_of_words:
        if(len(word)>longest_length):
            longest_length=len(word)
    return longest_length

list_of_words = ["manis", "anish", "pramish"]
longest_length = return_longest_word(list_of_words)
print(longest_length)