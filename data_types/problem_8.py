"""
Q.Python program to remove the nth index character from a nonempty string.
"""
non_empty_string = input("enter any word\n")
index = int(input("enter index you want to remove from the entered word\n"))

first_part_before_index = non_empty_string[0:index]
last_part_after_index = non_empty_string[index+1:]

print("The Final string after removing the required index is:", first_part_before_index+last_part_after_index)

