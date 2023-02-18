from .models import Books
from PyPDF2 import PdfFileReader
import fitz

def create_book(book_url):
    pages=[]
    book = fitz.open('media/'+str(book_url))
    for page_num in range(1,len(book)):
        page = book.load_page(page_num)
        page_text = page.get_text("text")
        pages.append(page_text)
    return pages


 

