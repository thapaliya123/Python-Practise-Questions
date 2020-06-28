#Python program to get a string from a given string where all occurrences of its first char
#have been changed to '$',
sample_string = input("enter any word")
first_char = sample_string[0]
sample_string_two=first_char
for i in range(1, len(sample_string)):
    if(sample_string[i]==first_char):
        sample_string_two = sample_string_two+"$"
    else:
        sample_string_two = sample_string_two+sample_string[i]
print(sample_string_two)