class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author 
        self.price = price

    def display_info(self):
        print(f"Title:{self.title}, Author: {self.author}, Price: {self.price}")


book_obj = Book("Harry Potter", "JK Rowling", 5000)
book_obj.display_info()

book1_obj = Book("Harry Potter", "JK Rowling", 50.00)

book1_obj.display_info()