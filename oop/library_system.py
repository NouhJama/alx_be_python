#Base Class
class Book:
    def __init__(self, title=str, author=str):
        self.title = title
        self.author = author
    
    #string representation of the Book object
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

#Derived Class
class EBook(Book):
    #has additional attribute file_size
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the constructor of the base class
        self.file_size = file_size  # in MB
    #string representation of the EBook object
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    #has additional attribute weight
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the constructor of the base class
        self.page_count = page_count  # in pages

    #string representation of the PrintBook object
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


#Composition
class Library:
    def __init__(self):
        self.books = []  # List to hold Book objects


    def add_book(self, book):
        if isinstance(book, Book): # Ensure only Book or its subclasses are added
            self.books.append(book)
        else:
            raise ValueError("Only Book instances can be added")

    def list_books(self):
        for book in self.books:
            print(book)