#Riccardo Giacalone

class Book:

    def __init__(self, title: str, author: str, isbn: int) -> None:
        self.title: str = title
        self.author: str = author
        self.isbn: int = isbn

    def __str__(self) -> str:
        f"book = {self.title}, {self.author}, {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str: str):
         return Book(book_str)

        
class Member:

    member_id:int = 0

    def __init__(self, name: str, member_id: int) -> None:
        self.name: str = name
        self.member_id: int = member_id + 1
        self.borrowed_books: list[Book] = []

    def borrow_book(self,book: Book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)

