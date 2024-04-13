import sqlite3
from decouple import config


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
        Database.make_users_table(fresh)
        Database.make_configs_table(fresh)
        Database.make_parcels_table(fresh)
        Database.make_persons_table(fresh)
        if fresh:
            Database.seed()

    @staticmethod
    def seed():
        Database.seed_users_table()
        Database.seed_configs_table()

    @staticmethod
    def make_users_table(fresh: bool = False):
        if fresh:
            Database.do("DROP TABLE IF EXISTS users;")
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uuid VARCHAR(15) UNIQUE,
                user_id BIGINT UNIQUE,
                role VARCHAR(15) DEFAULT "user",
                step INTEGER DEFAULT 0,
                status INTEGER DEFAULT 1,
                memory TEXT DEFAULT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT NULL
            );
        """
        Database.do(query)

    @staticmethod
    def make_configs_table(fresh: bool = False):
        if fresh:
            Database.do("DROP TABLE IF EXISTS configs;")
        query = """
            CREATE TABLE IF NOT EXISTS configs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(15),
                value TEXT DEFAULT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT NULL
            );
        """
        Database.do(query)

    @staticmethod
    def make_parcels_table(fresh: bool = False): 
        if fresh:
                Database.do("DROP TABLE IF EXISTS parcels;") # name of the table
        query = """
                CREATE TABLE IF NOT EXISTS parcels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender_id INTEGER,
                    receiver_id INTEGER,
                    country VARCHAR(30) DEFAULT NULL,
                    postal_code BIGINT UNIQUE DEFAULT 0,
                    address TEXT DEFAULT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """
        Database.do(query)

    @staticmethod
    def make_persons_table(fresh: bool = False): 
        if fresh:
                Database.do("DROP TABLE IF EXISTS persons;") # name of the table
        query = """
                CREATE TABLE IF NOT EXISTS persons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    card_id VARCHAR(20) UNIQUE DEFAULT NULL,
                    name VARCHAR(50) DEFAULT NULL
                );
            """
        Database.do(query)

    
    @staticmethod
    def seed_users_table():
        pass
        # from models.user import User

        # for admin in map(int, str(config("Admins")).split(",")):
        #     User.create(admin)


    @staticmethod
    def seed_configs_table():
        pass
        # from models.config import Config

        # Config.create("app_version", config("app_version"))


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
