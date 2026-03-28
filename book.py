from library_item import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.__author = author
    
    @property
    def author(self):
        return self.__author
    
    def __str__(self):
        return f"{super().__str__()}\nAuthor: {self.__author}"