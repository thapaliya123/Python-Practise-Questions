"""
29. Write a Python script to concatenate following dictionaries to create a new
one.
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
sample_list = [dic1, dic2, dic3]
concat_dict={}
for item in sample_list:
    concat_dict.update(item)

print(concat_dict)