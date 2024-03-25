"""
    Topic: Question9 / Assignment3
    Date: 15 Oct 2023
    Author: Juan Nicolas Randazzo

"""

L1 = [10, 20, 30, 10, 20, 40, 50]
D1 = {10: 0, 20: 0, 30: 0, 40: 0, 50: 0}

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0

for i in L1:
    if (i == 10):
        c1 += 1
        D1[10]= c1
    elif (i == 20):
        c2 += 1
        D1[20]= c2
    elif (i == 30):
        c3 += 1
        D1[30]= c3
    elif (i == 40):
        c4 += 1
        D1[40]= c4
    elif (i == 50):
        c5 += 1
        D1[50]= c5

print(D1)
