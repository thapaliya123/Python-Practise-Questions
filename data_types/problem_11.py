""""
Q.Python program to count the occurrences of each word in a given
sentence.
"""

sentence = "my name is anish thapaliya. my borther name is manish and pramish"
words = sentence.split(" ")
counts = dict()
for word in words:
    if word in counts:
        counts[word] = counts[word]+1
    else:
        counts[word] = 1
print(counts)
