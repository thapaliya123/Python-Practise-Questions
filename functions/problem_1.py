"""
1.Write a python function to find the max of three numbers
"""
def find_max_numbers(num1, num2, num3):
    if num1>num2:
        if(num1>num3):
            return f"reuturn max is {num1}"
        else:
            return f"return max is {num3}"

    else:
        if num2>num3:
            return f"max {num2}"
        else:
            return f"max {num3}"

print(find_max_numbers(1, 2, 3))