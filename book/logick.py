from .models import Books
from PyPDF2 import PdfFileReader
import fitz

def create_book(id):
    pages=[]
    book_id = Books.objects.get(id=id)
    url = book_id.book
    print(book_id.book)
    book = fitz.open('media/'+str(url))
    for page_num in range(len(book)):
        page = book.load_page(page_num)
        page_text = page.get_text("text")
        pages.append(page_text)
    return pages
        # page_book = Page.objects.create(book_id=id, text=f'Стр.  {page_num+1} \n\nСодержание;\n {page_text}')
