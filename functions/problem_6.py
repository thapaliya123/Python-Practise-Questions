"""
6.Write a python program to find whether a given number is in range
"""
def find_number_in_range(number, start, end):
    if number in range(start, end+1):
        return True
    else:
        return False

number = 20
start = 1
end = 21
print(find_number_in_range(number, start, end))
