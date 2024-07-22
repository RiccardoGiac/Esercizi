#Riccardo Giacalone

class Book:

    def __init__(self,book_id:str,title:str,author:str) -> None:
        self.book_id: book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
    
    def return_book(self):
        self.is_borrowed = False

class Member:

    def __init__(self,member_id:str,name:str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self,book:Book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
    
    def return_book(self,book:Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)

class Library:

    def __init__(self) -> None:
        self.books:dict[str,Book] = {}
        self.members:dict[str:Member] = {}

    def add_book(self,book_id:str,title:str,author:str):
        self.books[book_id] = Book(book_id,title,author)
    
    def register_member(self,member_id:str,name:str):
        self.members[member_id] = Member(member_id,name)
    
    def borrow_book(self,member_id:str,book_id:str):
        if member_id in self.members and book_id in self.books:
            self.members[member_id].borrow_book(self.books[book_id])
    
    def return_book(self,member_id:str,book_id:str):
        if member_id in self.members and book_id in self.books:
            self.members[member_id].return_book(self.books[book_id])
    
    def get_borrowed_books(self,member_id):
        return self.members[member_id].borrowed_books

        