"""
9.Write a Python function that takes a number as a parameter and check the
number is prime or not.
"""

def check_prime(number):
    flag=True
    for i in range(2, (number//2)+1):
        if(number%i==0):
            flag=False
    if flag==True:
        return "prime"
    else:
        return "not prime"
number = int(input("enter number you want check whether it is prime or not."))
print(check_prime(number))
