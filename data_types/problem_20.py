"""
Q.Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
"""
sample_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for item in sample_list:
    if(len(item)>2):
        if(item[0]==item[-1]):
            count=count+1
print(count)