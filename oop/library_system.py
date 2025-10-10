#Base Class
class Book:
    def __init__(self, title=str, author=str):
        self.title = title
        self.author = author

#Derived Class
class EBook(Book):
    #has additional attribute file_size
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the constructor of the base class
        self.file_size = file_size  # in MB

class PrintBook(Book):
    #has additional attribute weight
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the constructor of the base class
        self.page_count = page_count  # in pages

    
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
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")