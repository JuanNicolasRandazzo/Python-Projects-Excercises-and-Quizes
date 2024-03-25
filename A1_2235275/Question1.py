## +++++++++++++++++++++++++++++ Question 1 ++++++++++++++++++++++++++++++++++++++++++++++

print ("-------------------- Please enter the two numbers. Both has to be integers ---------------")
print ("Please enter the first integer : ", end="")
number1 = int(input())
print ("Please enter the second integer : ", end="")
number2 = int(input())

product  = number1 * number2
limitCondition = 1000
add  = number1 + number2

print ("The first number is : " , number1, " | The second number is : " , number2)


if product > limitCondition:
            print(number1, " + ",number2, " = ", add)



