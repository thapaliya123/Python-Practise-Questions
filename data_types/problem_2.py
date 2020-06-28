#program to extract first and last to character into new string
main_string = input("enter any word or letter\n")
main_string_len = len(main_string)

if(main_string_len>=2):
    partitioned_string=main_string[0:2]+main_string[main_string_len-2:main_string_len]
    print("The string made up of first two and last two character is:", partitioned_string)
else:
    print("Empty String")
