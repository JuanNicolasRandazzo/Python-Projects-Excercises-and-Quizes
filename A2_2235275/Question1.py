"""
    Topic: Question 1
    Date: 05 Oct 2023
    Author: Juan Nicolas Randazzo

"""

input_string = "PyNaTive"
lower_case = ""
upper_case = ""

for i in input_string:
    if i.islower():
        lower_case += i
    else:
        upper_case += i

print(lower_case + upper_case)
