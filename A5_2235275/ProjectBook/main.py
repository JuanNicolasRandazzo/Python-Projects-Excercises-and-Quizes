"""

    Topic: Question1/Assignment5
    Date: 12 Nov 2023
    Author: Juan Nicolas Randazzo

"""

from basisclasses.Book import Book

if __name__ == "__main__":

    print("+++++++++++++++++++++ Five Books")
    b1 = Book()
    b2 = Book(bookTitle = "A Wise Man's Fear",bookAuthor = "Patrick Rothfuss",bookEditor = "DAW Books " ,bookPrice = 20.0)
    b3 = Book("Cien Años de Soledad","Gabriel Garcia Marquez","Sudamericana",40)
    b4 = Book("Thus spoke Zarathustra", "Friedrich Nietzsche", "Ernst Horneffer", 3)
    b5 = Book("J'avue que j'ai vécu", "Pablo Neruda", "Matilde Urrutia", 2)
    b1.display()
    b2.display()
    b3.display()
    b4.display()
    b5.display()
