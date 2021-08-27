from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str, pages=100):
        self.content = content
        self.pages = pages


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class MobileFormatter(BaseFormatter):
    def format(self, book: Book):
        return book.content[:20]


class DesktopFormatter(BaseFormatter):
    def format(self, book: Book):
        return book.content[:100]


class Printer:
    def get_book(self, book: Book, formater: BaseFormatter):
        print('Print...')
        return formater.format(book)


printer = Printer()
book = Book('Hello there asfd 123456789456789456615456')
formater = MobileFormatter()
print(printer.get_book(book, formater))