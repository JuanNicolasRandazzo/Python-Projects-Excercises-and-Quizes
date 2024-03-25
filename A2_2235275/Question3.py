"""
    Topic: Question3
    Date: 05 Oct 2023
    Author: Juan Nicolas Randazzo
"""

s1 = "Pyai"
s2 = "Pynative"
storage = ""
for i in s1:
    if i in s2 and i not in storage:
        storage += i
print(storage)


if storage == s1:
    print("s1 and s2 are balanced True")
else:
    print("s1 and s2 are balanced False")
