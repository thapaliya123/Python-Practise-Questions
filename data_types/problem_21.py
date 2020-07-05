"""
Q.Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
"""
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(sample_list)):
    for  j in range(i+1):
        if(sample_list[i][-1]<sample_list[j][-1]):
            sample_list[i], sample_list[j] = sample_list[j], sample_list[i]
    
print(sample_list)