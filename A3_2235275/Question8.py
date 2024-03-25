"""
    Topic: Question8 / Assignment 3
    Date: 15 Oct 2023
    Author: Juan Nicolas Randazzo

"""

string1 = "pynativepynvepynative"
D1 = {'p': 0 ,'y': 0,'n':0,'a':0,'t':0,'i':0,'v':0,'e':0}
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0

for i in string1:
    if (i == "p"):
        c1 += 1
        D1["p"]= c1
    elif (i == "y"):
        c2 += 1
        D1["y"]= c2
    elif (i == "n"):
        c3 += 1
        D1["n"]= c3
    elif (i == "a"):
        c4 += 1
        D1["a"]= c4
    elif (i == "t"):
        c5 += 1
        D1["t"]= c5
    elif (i == "i"):
        c6 += 1
        D1["i"]= c6
    elif (i == "v"):
        c7 += 1
        D1["v"]= c7
    elif (i == "e"):
        c8 += 1
        D1["e"]= c8

print(D1)
