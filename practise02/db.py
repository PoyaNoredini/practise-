import sqlite3


class Database:
    @staticmethod
    def do(sql_query: str, parameters: tuple = ()):
        conn = sqlite3.connect("database.sqlite")
        cursor = conn.cursor()
        cursor.execute(sql_query, parameters)
        conn.commit()
        conn.close()

    @staticmethod
    def get(sql_query: str, parameters: tuple = ()):
        conn = sqlite3.connect("database.sqlite")
        cursor = conn.cursor()
        cursor.execute(sql_query, parameters)
        result = cursor.fetchall()
        conn.close()
        if result:
            return result
        else:
            return False

    @staticmethod
    def get_first(sql_query: str, parameters: tuple = ()):
        conn = sqlite3.connect("database.sqlite")
        cursor = conn.cursor()
        cursor.execute(sql_query, parameters)
        result = cursor.fetchall()
        conn.close()
        if result:
            return result[0]
        else:
            return False

    @staticmethod
    def migrate(fresh=False):
        Database.make_authors_table(fresh)
        Database.make_books_table(fresh)
        Database.make_publishers_table(fresh)
        Database.make_customers_table(fresh)
        Database.make_shops_table(fresh)
        Database.make_orders_table(fresh)
        Database.make_orderItems_table(fresh)
        Database.make_categories_table(fresh)
        Database.make_shops_books_table(fresh)
        if fresh:
            Database.seed()

    @staticmethod
    def seed():
        Database.seed_authors_table()
        Database.seed_books_table()  
        Database.seed_publishers_table()
        Database.seed_shops_table()
        Database.seed_customers_table()   
        Database.seed_orders_table()  
        Database.seed_orderItems_table()
        Database.seed_categories_table()
        Database.seed_shops_books_table()

    @staticmethod
    def make_authors_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS authors;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) DEFAULT NULL,
                birthday DATE DEFAULT NULL,
                nationality VARCHAR(25) DEFAULT NULL,
                biography TEXT DEFAULT NULL
            );
        """
        Database.do(query)
        
    @staticmethod
    def make_books_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS books;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30) DEFAULT NULL,
                price INTEGER DEFAULT 0, 
                author_id INTEGER,
                publisher_id INTEGER,
                category_id INTEGER
                
            );
        """
        Database.do(query)
        
    @staticmethod
    def make_publishers_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS publishers;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS publishers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                publisher_name VARCHAR(30) DEFAULT NULL,
                location TEXT DEFAULT NULL        
            );
        """
        Database.do(query)
        
        
    @staticmethod
    def make_shops_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS shops;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS shops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number VARCHAR(15) DEFAULT NULL,
                email VARCHAR(250) DEFAULT NULL,
                address TEXT DEFAULT NULL,
                fax_number INTEGER DEFAULT NULL
            );
        """
        Database.do(query)
        
        # id - phone_number - email - address - fax_number
        
        
    
    @staticmethod
    def make_shops_books_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS shops_books;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS shops_books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER DEFAULT NULL,
                shop_id INTEGER DEFAULT NULL,
                inventory INTEGER DEFAULT NULL
            );
        """
        Database.do(query)
        
        
    
        
    @staticmethod
    def make_customers_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS customer;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name VARCHAR(50) DEFAULT NULL,
                email VARCHAR(254) DEFAULT NULL,
                phone_number VARCHAR(15) DEFAULT NULL
                
            );
        """
        Database.do(query)
        
    @staticmethod
    def make_orders_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS orders;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER DEFAULT NULL,
                order_date DATETIME DEFAULT NULL,
                total_price DECIMAL(10, 2) DEFAULT 0.0,
                status VARCHAR(20) DEFAULT NULL,
                address TEXT DEFAULT NULL,
                postal_code VARCHAR(15) DEFAULT NULL
            );
        """
        Database.do(query)
        
    @staticmethod
    def make_orderItems_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS orderItems;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS orderItems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER DEFAULT NULL,
                book_id INTEGER DEFAULT NULL,
                number_book INTEGER DEFAULT NULL
            );
        """
        Database.do(query)
    
    @staticmethod
    def make_categories_table(fresh: bool = False): 
        if fresh:
            Database.do("DROP TABLE IF EXISTS categories;") # name of the table
        query = """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(255) DEFAULT NULL,
                parent_id INTEGER DEFAULT NULL
            );
        """
        Database.do(query)
    

    @staticmethod
    def seed_shops_books_table():
        pass
    
    @staticmethod
    def seed_categories_table():
        pass
    
    @staticmethod
    def seed_authors_table():
        pass

    @staticmethod
    def seed_books_table():
        pass

    @staticmethod
    def seed_publishers_table():
        pass

    @staticmethod
    def seed_shops_table():
        pass

    @staticmethod
    def seed_customers_table():
        pass

    @staticmethod
    def seed_orders_table():
        pass

    @staticmethod
    def seed_orderItems_table():
        pass

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python db.py <function_name>")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name.split(":")[0] == "migrate":
        if len(function_name.split(":")) == 2:
            fresh = function_name.split(":")[1] == "fresh"
        else:
            fresh = False

        if len(sys.argv) == 3:
            if hasattr(Database, f"make_{sys.argv[2]}_table"):
                method = getattr(Database, f"make_{sys.argv[2]}_table")
                if callable(method):
                    method(fresh)
                else:
                    print(f"make_{sys.argv[2]}_table is not a callable method.")
            else:
                print(f"No method found with the name make_{sys.argv[2]}_table.")
        else:
            if len(function_name.split(":")) == 2:
                fresh = function_name.split(":")[1] == "fresh"
            else:
                fresh = False
            Database.migrate(fresh)
