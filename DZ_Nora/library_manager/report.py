"""
Модуль report.py: Генерирует отчеты о книгах в библиотеке.

"""

def info_report():
    message = """
Модуль report.py - Генерирует отчеты о книгах в библиотеке.
"""
    return message

"""
TO DO

Функция `generate_report(library: Library)`: 
Генерирует отчет о всех книгах в библиотеке в формате строки.

"""
from catalog import library
def generate_report():
    print(f'Information about books in the library: \n{library.view_all_books()}' )

#generate_report()

#library.view_all_books()