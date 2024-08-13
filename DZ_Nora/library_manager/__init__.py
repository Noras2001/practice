summary = """

Здравствуйте, пакет \"library_manager\" инициализирован!

"""

print(summary)

"""
To DO
В корневом пакете `library_manager`:
     - Импортируйте основные компоненты пакета (`Library`, `generate_report`).
     - Определите `__all__` для управления экспортом.
"""
__all__ = ['info_catalog', 'info_report', 'info_formatting', 
           'info_data_validation', 'format_book_data', 'validate_book_data', 
           'library', 'Book']

from library_manager.catalog import info_catalog, library, Book

#from library_manager.report import info_report
from library_manager.utils.data_validation import info_data_validation, validate_book_data
from library_manager.utils.formatting import info_formatting, format_book_data
