import json

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def display_info(self):
        super().display_info()
        print(f"File Format: {self.file_format}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_all_books(self):
        for book in self.books:
            book.display_info()

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

class LibraryAPI:
    def __init__(self, database):
        self.database = database

    def add_book_to_database(self, book):
        data = json.load(open(self.database, 'r'))
        data['books'].append({'title': book.title, 'author': book.author, 'isbn': book.isbn})
        with open(self.database, 'w') as f:
            json.dump(data, f)

    def list_all_books_from_database(self):
        data = json.load(open(self.database, 'r'))
        return data['books']

    def delete_book_from_database(self, title):
        data = json.load(open(self.database, 'r'))
        for i, book in enumerate(data['books']):
            if book['title'].lower() == title.lower():
                del data['books'][i]
                with open(self.database, 'w') as f:
                    json.dump(data, f)
                return True
        return False

# Example usage
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
ebook1 = EBook("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", "PDF")

library = Library()
library.add_book(book1)
library.add_book(ebook1)

# Display all books in the library
library.display_all_books()

# Search for a book by title
searched_book = library.search_book_by_title("The Great Gatsby")
if searched_book:
    searched_book.display_info()
else:
    print("Book not found")

# Using the LibraryAPI to add, list, and delete books from the database
library_api = LibraryAPI("library_database.json")

# Add books to the database
library_api.add_book_to_database(book1)
library_api.add_book_to_database(ebook1)

# List all books from the database
print(library_api.list_all_books_from_database())

# Delete a book from the database
library_api.delete_book_from_database("The Catcher in the Rye")

# List all books after deletion
print(library_api.list_all_books_from_database())