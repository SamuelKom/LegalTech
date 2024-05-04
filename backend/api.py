import requests

API_KEY = ""
GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes?q="

def get_book(book_id):
    response = requests.get(GOOGLE_BOOKS_URL + book_id)
    if response.status_code == 200:
        print(response.text)
    else:
        print('Fehler beim GET-Request:', response.status_code)

get_book("Öffentliches+Recht+Ein+Basislehrbuch")