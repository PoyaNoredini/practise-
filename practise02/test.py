from db import Database 

from models.book import Book 
from models.author import Author
from models.shops_books import Shops_Books 

book_name = input('please enter the book name:')
books = Book.search_name(book_name)


for book in books :  

    
    #shops = book.shops()
     
    shops = book.shops()
    for shop in shops : 
        print( book.name, shop.address)
    
    #print(book.id, book.author.name)
    
     

