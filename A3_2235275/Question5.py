"""

    Topic: Question5
    Date: 14 Oct 2023
    Auhor: Juan Nicolas Randazzo

"""

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_diet = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

set_elements = set()

for i in roll_number:
    if (i in sample_diet.values()):
        set_elements.add(i)
print(f"The set elements are: {set_elements}")


set_elements.difference_update(set(sample_diet.values()))

print(set_elements)
