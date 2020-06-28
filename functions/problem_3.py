"""
3.Write a python function to multiply all the numbers in a list
"""

def mul_list_numbers(sample_list):
    mul=1
    for item in sample_list:
        mul = mul*item
    
    return f"The multiplication of numbers of list{sample_list} is {mul}"

sample_list=[1, 2, 3, 4, 5]
print(mul_list_numbers(sample_list))

