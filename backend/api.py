import requests
import os

var_name = "ISBN_DB_API_KEY"
if var_name in os.environ:
    var_value = os.environ[var_name]

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/"

def get_book_google(book_id):
    response = requests.get(GOOGLE_BOOKS_URL + "v1/volumes?q=" + book_id)

    if response.status_code == 200:
        data = response.json()

        for book in data['items']:
            if 'volumeInfo' in book:
                if 'title' in book['volumeInfo']:
                    print(book['volumeInfo']['title'], end='')
                else:
                    print("Title key does not exist for this book")
                
                if 'subtitle' in book['volumeInfo']:
                    print(": " + book['volumeInfo']['title'], end='')
                print()
    else:
        print('Fehler beim GET-Request:', response.status_code)

get_book_google("Detterbeck%2C+Steffen%3A+Öffentliches+Recht+–+Ein+Basislehrbuch+zum+Staatsrecht%2C+Verwaltungsrecht+und+Europarecht+mit+Übungsfällen")
