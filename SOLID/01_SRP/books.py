class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} from {self.author}"

class Library:
    def __init__(self, books: list[Book]):
        self.books = books

    def find_book(self, title: str):
        book = next((b for b in self.books if title == b.title), None)

        return book