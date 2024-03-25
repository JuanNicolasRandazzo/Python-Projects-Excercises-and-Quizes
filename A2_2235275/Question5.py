"""
    Topic: Question 5
    Date: 05 Oct 2023
    Author: Juan Nicolas Randazzo

"""

list_input = [54,44,27,79,91,41]
print(f"The original list is: {list_input}")
index4 = list_input.pop(4)
index2 = list_input.insert(1,index4)
last_index = list_input.append(index4)
print(f"The list after the change is: {list_input}")
