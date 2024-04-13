from db import Database




class Author :
    
    def __init__(self , id:int):
        self.id :int = id
        if self.is_exist(id) : 
           self.sync()
            
        
        # brithday notinality biographa
    def sync (self) -> bool:
        
        all_data = Database.get_first(
             f"SELECT * FROM `authors` WHERE id = ?", (self.id,)
        )
        if all_data:    
            self.id :int = int(all_data[0])
            self.name : str = str(all_data[1])
            self.brithday : str = str(all_data[2])
            self.notinality : str = str(all_data[3])
            self.biography : str = str(all_data[4])
            
            
            return True
        else:
            return False 
        
    @staticmethod
    def is_exist(id: int) -> bool:
        result = Database.get(f"SELECT * FROM `authors` WHERE `id` = ?", (id,))
        if result:
            return True
        else:
            return False
    @staticmethod    
    def search_name(name: str) :
        author_data = Database.get('SELECT * FROM `authors` WHERE `name` LIKE ?' , (f"%{name}%", ))
        authors= []
        
        for author in author_data: 
            authors.append(Author(author[0]))
            
        return authors
            