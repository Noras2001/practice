"""
Модуль catalog.py - Управляет книгами в библиотеке, 
включая добавление, удаление и поиск.
"""

def info_catalog():
    message = """
Модуль catalog.py - Управляет книгами в библиотеке, 
включая добавление, удаление и поиск.
"""
    return message

"""
TO DO

Класс `Library` для управления книгами. Класс должен включать методы для:
       - Добавления книги (с атрибутами: название, автор, жанр).
       - Удаления книги по названию.
       - Поиска книги по названию, автору и жанру.
       - Просмотра всех книг в библиотеке.
"""

class Book:
    def __init__(self, name: str, author: str, genre: str):
        """
        :param name: Title of the book
        :param author: Author of the book
        :param genre: Genre of the book
        """
        self.name = name       
        self.author = author
        self.genre = genre
    
    def __str__(self):
        """
        String representation of the object"""
        return f"Title: {self.name}, Author: {self.author}, Genre: {self.genre}"
        
    def __repr__(self):
        return f"Book(name='{self.name}', author='{self.author}', genre='{self.genre}')"
    
    def capitalize_fields(self):
        """
        Capitalizes the name, author and genre fields (in order to simplify the search)
        """
        self.name = self.name.capitalize()
        self.author = self.author.capitalize()
        self.genre = self.genre.capitalize()

    def display_info(self):
        """
        Displays the book's information
        """
        print(f"Title: {self.name};\nAuthor: {self.author};\nGenre: {self.genre}.")


class Library:
    def __init__(self):
        """
        Empty list to add books to  the library.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a new book to the library.
        """
        self.books.append(book)
        print(f'Book "{book.name}" by {book.author} added to the library.')

    def remove_book(self, name: str):
        """
        Removes a book from the library by the title
        :param name: Title of the book to be removed
        """
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
                print(f'Book "{name}" removed from the library.')
                return
        print(f'Book "{name}" not found in the library.')

    def search_books(self, name: str = None, author: str = None, genre: str = None):
        """
        Searches for books in the library by the title, author, genre or its part.

        :param name: (Optional) Title of the book to search for.
        :param author: (Optional) Author of the book to search for.
        :param genre: (Optional) Genre of the book to search for.
        :return: List of books matching the search criteria.

        """
        found_books = [] #empty list to collect the found books
        for book in self.books:
            if (name and name.capitalize() in book.name) or (author and author.capitalize() in book.author) or (genre and genre.capitalize() in book.genre):
                found_books.append(book)
        
        if found_books:
            print("Search results:")
            for book in found_books:
                book.display_info()
        else:
            print("No books found matching the search criteria.")
        return found_books

    def view_all_books(self):
        """
        Displays all the books currently in the library.
        """
        if not self.books:
            print("The library is currently empty.")
        else:
            print("Books currently in the library:")
            for book in self.books:
                book.display_info()



# test this module
# test of the class Book()
book_01 = Book('One flew over cuckoos nest', 'Ken Kesay', 'Tragedey')
book_02 = Book('Ana Karenina', 'Leo Tolstoy', 'Drama')
book_03 = Book('The Time of the Hero', 'Mario Vargas Llosa', 'Drama')
book_04 = Book('The Great Gatsby', 'F. Scott Fitzgerald', 'Drama')
book_05 = Book('The Catcher in the Rye', 'J.D. Salinger', 'Drama')  
book_01.display_info()  

#test of the class Library()
library = Library()
library.add_book(book_01)
library.add_book(book_02)
library.add_book(book_03)
library.add_book(book_04)
library.add_book(book_05)
library.view_all_books()
library.search_books(author='George Orwell')
library.search_books(author='Leo')
library.remove_book(name='Ana Karenina')
print('- *20')
library.view_all_books()
library.search_books(name='Ana')


