from db import Database

from .book import Book
from .shop import Shop

class Shops_Books : 
    
    def __init__(self , id:int):
       self.id :int = id
       if  self.is_exist(id) : 
           self.sync()
            

    def sync (self) -> bool:
        
        all_data = Database.get_first(
             f"SELECT * FROM `shops_books` WHERE id = ?", (self.id,)
        )
        if all_data:    
            self.id :int = int(all_data[0])
            self.book_id : Book = Book(all_data[1])
            self.shop_id : Shop = Shop(all_data[2])
            self.inventory : int = int(all_data[3])
            
            return True
        else:
            return False 

    
    @staticmethod
    def is_exist(id: int) -> bool:
        result = Database.get(f"SELECT * FROM `shops_books` WHERE `id` = ?", (id,))
        if result:
            return True
        else:
            return False
        
    @staticmethod
    def search_book_id(id: int):
        shop_data = Database.get(f"SELECT * FROM `shops_books` WHERE `book_id` = ?", (id,))
        shops = []
        
        if shop_data:
            for shop in shop_data : 
                shops.append(Shop(shop[2])) # shop_id
            
        return shops

       

        
      