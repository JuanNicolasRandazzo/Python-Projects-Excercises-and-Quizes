"""
    Topic: Question2/Assignment5
    Date: 13 Nov 2023
    Author: Juan Nicolas Randazzo

"""
import math

class Circle:

    __cir = 1

    def __init__(self, radius = 0.0, color = "Red"):

        self.__radius = radius
        self.__color = color
        self.__circleId = Circle.__cir
        Circle.__cir += 1


    ### Getters and Setters

    ## Radius

    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, r):

        if r == None or r <= 0 or r == "":

            print(f"Error: The radius cannot be set as {r}.")

        else:

            self.__radius = r

    ## Color

    def getColor(self):
        return self.__color

    def setColor(self,cl):

        if cl is None or cl.isdigit() or cl == "":

            print(f"Error: The color cannot be set as {cl}.")

        else:

            self.__color = cl


    ##Circle Id

         
    def getCircleId(self):
        return self.__circleId
            
    ## Methods

    def calculatePerimeter(self):
        return 2 * math.pi * self.__radius

    def calculateArea(self):
        return math.pi * (self.__radius ** 2)

    ## Instance Level Methods
    def display(self):
        print(f"Circle Id: CIR_{self.__circleId}, Radius: {self.__radius}, Color: {self.__color}, Perimeter:{self.calculatePerimeter()}, Area: {self.calculateArea()}")
