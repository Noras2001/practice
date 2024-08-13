from library_manager import library, Book

#from library_manager import info_catalog, info_report, info_formatting, info_data_validation

# print(f'{info_catalog()}\n {info_report()}\n {info_data_validation()}\n {info_formatting()}')




book_01 = Book('One flew over cuckoos nest', 'Ken Kesay', 'Tragedey')
library.add_book(book_01)
book_02 = Book('Ana Karenina', 'Leo Tolstoy', 'Drama')
library.add_book(book_02)
#library.add_book(book_03)
#library.add_book(book_04)
#library.add_book(book_05)
library.view_all_books()
library.search_books(author='George Orwell')
print('-+'*20)

#library.remove_book(name='Ana Karenina')
print('-+'*20)
library.view_all_books()
print('-+'*20)
library.search_books(name='Ana')
print('-+'*20)
library.search_books(author='Leo')
print('- '*20)









