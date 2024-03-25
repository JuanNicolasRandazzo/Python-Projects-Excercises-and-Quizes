"""
    Topic: Question 2
    Date: 05 Oct 2023
    Author: Juan Nicolas Randazzo

"""

input_string = "sTRinG10@"

lower_case = 0
upper_case = 0
numbers = 0
characters = 0
for i in input_string:
    if i.islower():
        lower_case += 1
    elif i.isupper():
        upper_case += 1
    elif i.isdigit():
        numbers += 1
    else:
        characters += 1

print("The string is: ", input_string)
print(" Lower case: ", lower_case)
print(" Upper case: ", upper_case)
print(" Numbers: ", numbers)
print(" Characters: ", characters)
