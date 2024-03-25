"""
    Topic: Calss Person / Assignment6
    Date: 15 Nov 2023
    Author: Juan Nicolas Randazzo

"""


class Person:


    def __init__(self, lastName,firstName,phoneType):

        self._lastName = lastName
        self._firstName = firstName
        self._phoneType = phoneType


    ### Last Name

    def getLastName(self):
        return self._lastName

    def setLastName(self,ln):
        self._lastName = ln

    ### First Name

    def getFirstName(self):
        return self._firstName
    def setFirstName(self,fn):
        self._firstName = fn

    ### Phone Type

    def getPhoneType(self):
        return self._phoneType
    def setPhoneType(self, pt):
        self._phoneType = pt


    def __str__(self):

        return f"First Name: {self._firstName}, Last Name: {self._lastName}, Phone: {self._phoneType} "


class CertificationExam:


    def __init__(self, iD, title, successMark, nodw):

        self._iD = iD
        self._title = title
        self._successMark = successMark
        self._nodw = nodw

    ### ID

    def getID(self):
        return self._iD

    ###Title

    def getTitle(self):
        return self._title

    ### SuccessMark

    def getSuccessMark(self):
        
        return self._successMark
    

    def setSuccessMark(self, sm):

        self._successMark = sm

    ### Numbers of days to wait

    def getNumbersOfDaysToWait(self):

        return self._nodw

    def setNumbersOfDaysToWait (self, nw):
        self._nodw = nw


    def __str__(self):

        return f"ID: {self._iD}, Title: {self._title}, Success Mark: {self._successMark}, Number of Days to Wait: {self._nodw} "
