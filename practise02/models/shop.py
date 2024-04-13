from db import Database




class Shop : 
    
    def __init__(self , id:int):
       self.id :int = id
       if  self.is_exist(id) : 
           self.sync()
            


# id - phone_number - email - address - fax_number

    def sync (self) -> bool:
        
        all_data = Database.get_first(
             f"SELECT * FROM `shops` WHERE id = ?", (self.id,)
        )
        if all_data:    
            self.id :int = int(all_data[0])
            self.phone_number :str = str(all_data[1])
            self.email : str = str(all_data[2])
            self.address : str = str(all_data[3])
            self.fax_number : int = int(all_data[4])
            
            return True
        else:
            return False 

   

    @staticmethod
    def is_exist(id: int) -> bool:
        result = Database.get(f"SELECT * FROM `shops` WHERE `id` = ?", (id,))
        if result:
            return True
        else:
            return False
        
    def books(self): 
        from .book import Book
        book_data = Database.get(f"SELECT * FROM `shops_books` WHERE `book_id` = ?", (self.id,))
        books = []
        
        if book_data: 
         for book in book_data :    
                books.append(Book(book[1])) 
            
        return books