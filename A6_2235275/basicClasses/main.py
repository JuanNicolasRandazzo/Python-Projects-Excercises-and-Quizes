"""
    Topic: Main / Assignment 6
    Date: 25 Nov 2023
    Author: Juan Nicolas Randazzo

"""
from Person import Person, CertificationExam
from Candidate import Candidate
from DoCertificationExam import DoCertificationExam

if __name__ == "__main__":

    java_exam = CertificationExam("1z0-151", "Java", 70, 7)
    python_exam = CertificationExam("1z0-147", "Python", 75, 7)

    candidate = Candidate("Doe", "John", "123-456-7890","2023-11-23", java_exam,30)

    

    print("Java Exam Information:")
    print(java_exam)
    print("Python Exam Information:")
    print(python_exam)
    print("Candidate1 Information:")
    print(candidate)
   
    
    
