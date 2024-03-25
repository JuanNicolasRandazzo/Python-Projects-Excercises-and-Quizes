"""

    Topic: Questio6 / Assignment3
    Date: 15 Oct 2023
    Author: Juan Nicolas Randazzo

"""

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
L1 = []



for i in speed.values():
    
    if i not in L1:
        L1.append(i)

print(f"The list is:{L1}")
