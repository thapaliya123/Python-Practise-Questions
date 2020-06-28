"""
19. Write a Python program to create Fibonacci series upto n using Lambda.
"""
def generate_fibonacci_series(number):
    first = 0
    second = 1
    print(f"{first} {second}", end=" ")
    for i in range(2, number):
        third = first+second
        print(f"{third}", end=" ")
        first = second
        second=third
    print("\n")
number = int(input("enter the number of iitem in series"))
generate_fibonacci_series(number)

"""
20. Write a Python program to find intersection of two given arrays using
Lambda.
"""
intersection_two_list = lambda list1, list2: set(list1).intersection(set(list2))
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [5,6,7,8,9]
print(intersection_two_list(list1, list2))