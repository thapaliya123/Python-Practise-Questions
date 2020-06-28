"""
5.Write a python function to find factorial of a given non negativenumber
"""

def find_factorial(number):
    mul=1
    for i in range(1, number+1):
        mul=mul*i
    return f"The facorial of {number} is {mul}"

number = 5
print(find_factorial(5))