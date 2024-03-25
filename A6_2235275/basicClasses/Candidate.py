"""
    Topic: Candidate Class / Assignment6
    Date: 15 Nov 2023
    Author: Juan Nicolas Randazzo

"""

from Person import Person, CertificationExam


class Candidate(Person):

    def __init__(self,lastName,firstName,phoneType, examDate, certificationExam,examMark,):

        super().__init__(lastName,firstName,phoneType)

        self._examDate = examDate
        self._certificationExam = certificationExam
        self._examMark = examMark
        self._grade = None
        self._nbDaysToWait = None

    ### Exam Date

    def getExamDate(self):

        return self._examDate
    def setExamDate(self, ed):

        self._examDate = ed

    ### Exam Mark

    def getExamMark(self):

        return self._examMark

    def setExamMark(self,em):

        self._examMark = em

    ### Certification Exam

    def getCertificationExam(self):

        return self._certificationExam

    def setCertificationExam(self, ce):

        self._certificationExam = ce

    ### Methods

    def serviceSuccess (self,grade):

        self._grade = grade

    def serviceFaillure (self, nbDaysToWait):
        
        self._grade = "E"
        self._nbDaysToWait = nbDaysToWait


    ### Override String

    def __str__(self):

        if self._grade is not None:
            
            return f"Pass Certification exam: {self._grade} . Certification Exam id: {self._certificationExam.getID}. Exam Title: {self._certificationExam.getTitle()} .Mark: {self._examMark}"

        elif self._nbDaysToWait is not None:

            return f"Fails Certification exam. Certification Exam id: {self._certificationExam.getID()}. Exam Title: {self._certificationExam.getTitle()}. Mark: {self._examMark}. Number Of Days to Wait: {self._nbDaysToWait}"

        else:
            return super().__str__()
