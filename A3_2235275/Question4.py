"""

    Topic: Question4/Assignment3
    Date: 13 Oct 2023
    Author: Juan Nicolas Randazzo

"""

first_Set = {27, 43, 34}
second_Set = {34, 93, 22, 27, 43, 53, 48}

subset_test = first_Set.issubset(second_Set)
print(f"Second set is a subset of the first set: {subset_test}")
print(f"First set is a subset of the second set : {second_Set.issubset(first_Set)}")


if subset_test:
     first_Set.clear()

print(f"First Set removed: {first_Set}")
     
