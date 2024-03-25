"""
    Topic: Question4/Assignment4
    Date: 27 OCT 2023
    Author: Juan Nicolas Randazzo

"""


armstrong = lambda num: num == sum(map(lambda x: int(x) ** 3, str(num)))


number = int(input("Enter a number: "))

result = list(filter(armstrong, [number]))

if result:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
