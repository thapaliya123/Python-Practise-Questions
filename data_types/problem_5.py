"""
Q.Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
"""

sample_string = input("Enter any word or string\n")
if(len(sample_string)>=3):
    last_three_character = sample_string[len(sample_string)-3:len(sample_string)]
    if(last_three_character=='ing'):
        sample_string=sample_string+"ly"
        print("string after adding ly:", sample_string)
    else:
        sample_string=sample_string+"ing"
        print("string after adding ing:", sample_string)
else:
    print("Length of string is less than 3 and string is:", sample_string)