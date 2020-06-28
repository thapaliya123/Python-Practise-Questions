"""
7.Write a python program that accepts a string and calculate the number of upper case letters
and lower case letters
"""

def find_upper_lower_case_number(sample_string):
    upper_count = 0
    lower_count = 0
    for char in sample_string:
        if char!=" ":
            if char.isupper()==True:
                upper_count = upper_count+1
            else:
                lower_count = lower_count+1
    return f"Upper case count is{upper_count}\nlower case count is {lower_count}"

    
sample_string = "The quick Brown Fox"
print(find_upper_lower_case_number(sample_string))