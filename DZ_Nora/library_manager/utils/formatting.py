"""
Модуль formatting.py - Функции для форматирования данных книг для отчетов.
"""
def info_formatting():
    message = """
Модуль formatting.py - Функции для форматирования данных книг для отчетов.
"""
    return message

"""
TO DO
"""
def format_book_data(data: dict) -> str:
    """
    Formats book data to a string 

    :param data: A dictionary containing book information with keys 'title', 'author', and 'genre'.
    :return: A formatted string in the format 'Title: {title}, Author: {author}, Genre: {genre}'.
    """
    # Extracting the relevant information from the dictionary
    title = data.get('title', 'Unknown Title')
    author = data.get('author', 'Unknown Author')
    genre = data.get('genre', 'Unknown Genre')

    # Formatting the data into a single string
    formatted_string = f"Title: {title}, Author: {author}, Genre: {genre}"

    return formatted_string

# test of this function
def format_book_data(data: dict) -> str:
    """
    Formats book data into a string suitable for reporting.

    :param data: A dictionary containing book information with keys 'title', 'author', and 'genre'.
    :return: A formatted string in the format 'Title: {title}, Author: {author}, Genre: {genre}'.
    """
    # Extracting the relevant information from the dictionary
    title = data.get('title', 'Unknown Title')
    author = data.get('author', 'Unknown Author')
    genre = data.get('genre', 'Unknown Genre')

    # Formatting the data into a single string
    formatted_string = f"Title: {title}, Author: {author}, Genre: {genre}"

    return formatted_string

# test of the function format_book_data
# book_data = {
#     'title': '1984',
#     'author': 'George Orwell',
#     'genre': 'Dystopian'
# }
# report_string = format_book_data(book_data)
# print(report_string) 

