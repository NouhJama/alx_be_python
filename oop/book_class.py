class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    #Destructor to clean up resources if needed
    def __del__(self):
        print(f"Deleting {self.title}")

    #String representation of the book object
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    #Official representation of the book object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"