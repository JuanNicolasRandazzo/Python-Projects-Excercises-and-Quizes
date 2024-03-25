"""
    Topic: Question7/Assignment3
    Date: 15 Oct 2023
    Author: Juan Nicolas Randazzo

"""

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

elements = tuple(set(sampleList))


min_number = min(elements)
max_number = max(elements)


print(f"Unique elements as tuple: {elements}" )
print(f"Minimum number: {min_number}")
print(f"Maximum number: {max_number}")
