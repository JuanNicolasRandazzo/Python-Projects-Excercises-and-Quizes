"""
    Topic: Question2/Assignment3
    Date: 12 Oct 2023
    Author: Juan Nicolas Randazzo

"""

sampleList = ['a', 'c', 'b', 'd', 'd', 'a', 'e', 'a', 'e']

D1 = {'a': 0 ,'b': 0,'c':0,'d':0,'e':0 }
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0

for i in sampleList:
    if (i == "a"):
        c1 += 1
        D1["a"]= c1
    elif (i == "b"):
        c2 += 1
        D1["b"]= c2
    elif (i == "c"):
        c3 += 1
        D1["c"]= c3
    elif (i == "d"):
        c4 += 1
        D1["d"]= c4
    elif (i == "e"):
        c5 += 1
        D1["e"]= c5
        
print(D1)
        
