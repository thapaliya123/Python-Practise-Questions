"""
2.Write the python function to sum all the numbers in a list
"""
def sum_list_numbers(sample_list):
    sum=0
    for item in sample_list:
        sum=sum+item
    return sum

sample_list = [8, 2, 3, -1, 7]
print(f"The sum numbers in list {sample_list} is {sum_list_numbers(sample_list)}")