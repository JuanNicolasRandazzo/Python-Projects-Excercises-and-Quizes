"""
    Topic: Class Certification Exam / Assignment6
    Date: 15 Nov 2023
    Author: Juan Nicolas Randazzo

"""
from Person import Person, CertificationExam
from Candidate import Candidate

class DoCertificationExam():

    def __init__(self, candidate):

        self._candidate = candidate
        self._javaObj = CertificationExam("1z0-151","Java")
        self._pythonObj = CertificationExam("1z0-147","Python")
        self.validateCertification()


    def getCandidate(self):

        return self._candidate
    
    def setCandidate(self,c):

        self._candidate = c

    def getJavaObj(self):

        return self._javaObj

    def setJavaObj(self,jo):

        self._javaObj = jo

    def getPythonObj(self):

        return self._pythonObj

    def setPythonObj(self,po):

        self._pythonObj = po


    @staticmethod
    def getGrade(self,examMark):

        examMark = self._Candidate.getExamMark()

        if examMark < 60:

            grade = "E"

        elif examMark >= 60 and examMark < 65:

            grade = "D"

        elif examMark >= 65 and examMark < 70:

            grade = "D+"

        elif examMark >= 70 and examMark < 75:

            grade = "C"

        elif examMark >= 75 and examMark < 80:

            grade = "C+"

        elif examMark >= 80 and examMark < 85:

            grade = "B"
            
        elif examMark >= 85 and examMark < 90:

            grade = "B+"
            
        elif examMark >= 90 and examMark < 95:

            grade = "A"

        elif examMark >= 95:

            grade = "A+"

        return grade

    

    def getMark(self,examID, lastName):

        examID = self._CertificationExam.getID()
        lastName = self._Person.getLastName()
        
        with open("./Mark.txt", 'r') as rf:

                f_content = rf.readline()
                while f_content:

                    split_content = f_content.strip().split(",")
                    print(f"{split_content}", end="\n")
                    
                    f_content = rf.readline()
                    
                    if examID == split_content[0] and lastName == split_content[1]:

                            print(f"{split_content[2]}",end="\n")
                            
                            examMark = split_content[2]
                            
                            break
                    else:

                            print("Error: Exam Id or Last Name does not exist in the system.")

        return  examMark
            
        

        

    def validateCertification(self):
        
        certification = self._Candidate.getCertificationExam()
        examMark = self._getMark()
        
        if examMark is not None and examMark >= 60:
            
            grade = self.getGrade(examMark)

            
            self._candidate.serviceSuccess(grade)
        else:
             self._candidate.serviceFaillure(30) 



    
    
    def __str__(self):

        return """(examMark >=95) → A+
                (examMark >=90 && examMark<95) → A
                (examMark >=85 && examMark<=90) → B+
                (examMark >=80 && examMark<=85) → B
                (examMark >=75 && examMark<=80) → C+
                (examMark >=70 && examMark<=75) → C
                (examMark >=65 && examMark<=70) → D+
                (examMark >=60 && examMark<=65) → D
                (examMark <60) → E """
        
