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

    m_id:int = 0

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.member_id: int = Member.m_id
        self.borrowed_books: list[Book] = []
        Member.m_id += 1

    def borrow_book(self,book: Book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
        else:
            print("Book already borrowed")

    def return_book(self,book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print("Book isn't borrowed")

    def __str__(self) -> str:
        f"Member = {self.name}, {self.member_id}, {self.borrowed_books}"

    @classmethod
    def from_string(cls,member_str :str):
        return Member(member_str)
    

class Library:

    total_books: int = 0

    def __init__(self, books: list[Book] = [], members: list[Member]=[]) -> None:
        self.books: list[Book] = books
        self.members: list[Member] = members
    
    def add_book(self, book: Book):
        self.books.append(book)
        Library.total_books += 1

    def remove_book(self,book: Book):
        self.books.remove(book)
        Library.total_books -= 1

    def register_member(self, member:Member):
        self.members.append(member)

    def lend_book(self, book:Book, member:Member):
        if book in self.books:
            member.borrow_book(book)
            self.books.remove(book)
        else:
            print(f"{book} is not in the Library")
    
    def __str__(self) -> str:
        f"{self.books}, {self.members}"

    @classmethod
    def library_statistics(cls):
        print(Library.total_books)

    

    