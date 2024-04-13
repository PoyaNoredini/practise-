from db import Database

from .author import Author
from .shop import Shop

# id - name - price - author_id pulished_id category_id

class Book :
    
    def __init__(self , id:int):
        self.id :int = id
        if self.is_exist(id) : 
           self.sync()
            
        
        
    def sync (self) -> bool:
        
        all_data = Database.get_first(
             f"SELECT * FROM `books` WHERE id = ?", (self.id,)
        )
        if all_data:    
            self.id :int = int(all_data[0])
            self.name : str = str(all_data[1])
            self.price : int = int(all_data[2])
            self.author : Author = Author(all_data[3])
            self.published_id : int = int(all_data[4])
            self.category_id : int = int(all_data[5])
            
            return True
        else:
            return False 
        
    def shops(self):
        shop_data = Database.get(f"SELECT * FROM `shops_books` WHERE `book_id` = ?", (self.id,))
        shops = []
        
        if shop_data:
            for shop in shop_data : 
                shops.append(Shop(shop[2])) # shop_id
            
        return shops

        
    @staticmethod
    def is_exist(id: int) -> bool:
        result = Database.get(f"SELECT * FROM `books` WHERE `id` = ?", (id,))
        if result:
            return True
        else:
            return False
    @staticmethod    
    def search_name(name: str) :
        books_data = Database.get('SELECT * FROM `books` WHERE `name` LIKE ?' , (f"%{name}%", ))
        books= []
        
        if books_data :
            for book in books_data: 
                books.append(Book(book[0]))
                
            return books
        else :
            return False
                