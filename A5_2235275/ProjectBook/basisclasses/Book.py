
"""

    Topic: Question1/ Assignment5
    Date:  12 Nov 2023
    Author: Juan Nicolas Randazzo


"""

class Book:


    __seq = 1

    def __init__(self,bookTitle = "The Brothers Karamazov",bookAuthor = "Fiodor Dostoyevski",bookEditor = "The Russian Messenger" ,bookPrice = 10.0):


        self.__bookTitle = bookTitle
        self.__bookAuthor = bookAuthor
        self.__bookEditor = bookEditor
        self.__bookPrice = bookPrice
        self.__bookId = Book.__seq
        Book.__seq += 1




    ### Getters and Setters

        
    ##Book Title
        
    def getBookTitle(self):
        return self.__bookTitle
    
    def setBookTitle(self,bt):

        if bt is None or bt.isdigit() or bt == "":
            print(f"Error: The Book title cannot be set as {bt}.")
        else:
            
            self.__bookTitle = bt

    ##Book Author

    def getBookAuthor(self):

        return self.__bookAuthor

    def setBookAuthor(self,ba):

        if ba is None or ba.isdigit() or ba == "":
            print(f"Error: The Book author cannot be set as {ba}.")
        else:
            self.__bookAuthor = ba


    ##Book Edit

    def getBookEditor(self):

        return self.__bookEditor

    def setBookEditor(self,be):

        if be is None or be.isdigit() or be == "":
            print(f"Error: The Book editor cannot be set as {be}.")
        else:
            self.__bookEditor = be

    ##Book Price

    def getbookPrice(self):

        return slef.__bookPrice

    def setbookPrice(self,bp):

        if bp == None or bp < 0 or bp == "":
            print(f"Error: The Book price cannot be set as {bp}.")
        else:
            self.__bookPrice = bp

    ##Book Id
    def getBookId(self):
        return self.__bookId


    ## Instance Level Methods
    def display(self):
        print(f"Book Id: {self.__bookId}, Book Name: {self.__bookTitle}, Author Name: {self.__bookAuthor}, Price: ${self.__bookPrice}")


    
        
    
         
        
        
