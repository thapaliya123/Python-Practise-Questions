"""
Q.Write a Python program to remove duplicates from a list.
"""
sample_list = [1, 2, "anish", 2, "anish"]
list_unique = {item for item in sample_list}
counts = dict()
for item in sample_list:
    if item in counts:
        counts[item] = counts[item]+1
    else:
        counts[item] = 1
for key, value in counts.items():
    if value>=2:
        for i in range(value-1):
            sample_list.remove(key)
print(sample_list)