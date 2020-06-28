"""
Q.a Python function to insert a string in the middle of a string.
"""
def string_in_middle(target_string, inset_string):
    target_string = target_string[0:2]+inset_string+target_string[2:]
    return target_string

print(string_in_middle('[[]]<<>>', 'Python'))
print(string_in_middle('{{}}', 'PHP'))