"""
Модуль data_validation.py - Функции для валидации данных книг.
"""

def info_data_validation():
    message = """
Модуль data_validation.py - Функции для валидации данных книг.
    """
    return message

"""
TO DO
Функция `validate_book_data(data: dict) -> bool`: Проверяет корректность данных книги. 
Например, проверяет, 
что все обязательные поля присутствуют и корректны.
"""

def validate_book_data(data: dict) -> bool:
    """
    Validates the book data to ensure that all required fields are present and OK.

    :param data: A dictionary containing book information.
    :return: True if the data is valid, False otherwise.
    """
    
    required_fields = ['title', 'author', 'genre']

    # Check if all required fields are present
    for field in required_fields:
        if field not in data:
            print(f"Missing required field: {field}")
            return False

        # Check if the field is not empty and is of the correct type
        if not isinstance(data[field], str) or not data[field].strip():
            print(f"Invalid value for field: {field}")
            return False

    # If everything is OK -> returns True
    return True

# test
# book_data_valid = {
#     'title': 'The Great Gatsby',
#     'author': 'F. Scott Fitzgerald',
#     'genre': 'Classic Fiction'
# }

# # with the correct book data
# is_valid = validate_book_data(book_data_valid)
# print(is_valid)

# book_data_invalid = {
#     'title': '',
#     'author': 'F. Scott Fitzgerald',
#     'genre': 'Classic Fiction'
# }

# # the incorrect book data
# is_valid = validate_book_data(book_data_invalid)  # Output: False, with an error message


