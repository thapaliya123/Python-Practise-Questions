"""
4.Python program to reverse a string
"""
def reverse_string(sample_string):
    return sample_string[-1::-1]

sample_string = "1234abcd"
print(reverse_string(sample_string))