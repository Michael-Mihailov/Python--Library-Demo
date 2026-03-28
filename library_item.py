class LibraryItem:
    def __init__ (self, title, item_id):
        self.__title = title
        self.__item_id = item_id
        self.__checked_out = False

    @property
    def title(self):
        return self.__title
    
    @property
    def item_id(self):
        return self.__item_id
    
    @property
    def checked_out(self):
        return self.__checked_out
    
    def check_out(self):
        if not self.checked_out:
            self.__checked_out = True
            return True
        return False
    
    def return_item(self):
        if self.checked_out:
            self.__checked_out = False
            return True
        return False
    
    def __str__(self):
        return f"Title: {self.title}\nItem ID: {self.item_id}\nChecked Out: {self.checked_out}"