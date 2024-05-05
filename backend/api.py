import requests
import os

#from dotenv import load_dotenv

#load_dotenv('.env') 

#ISBN_DB_API_KEY = os.environ.get('ISBN_DB_API_KEY')

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"
#ISBN_DB_API_URL = "https://api2.isbndb.com/books/"

def get_book_google(author, title, year):
    #payload = {'column': 'title'}
    #headers = {'Authorization': 'application/json'}
    params = {
        "q": f'intitle:"{title}"+inauthor:"{author}"'
    }
    response = requests.get(GOOGLE_BOOKS_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        newestVersionYear = year
        for book in data['items']:
            if 'volumeInfo' in book:
                volumeInfo = book['volumeInfo']
                if 'title' in volumeInfo and 'publishedDate' in volumeInfo and 'authors' in volumeInfo:
                    #print(book['volumeInfo']['title'] + ", " + book['volumeInfo']['publishedDate'], end=', ')
                    #print(volumeInfo['authors'])
                    volumeYear = volumeInfo['publishedDate'].split("-")[0]
                    #print(volumeYear)
                    if volumeYear > newestVersionYear:
                        newestVersionYear = volumeYear
                #else:
                #    print("title, date or author empty")
                
                #if 'subtitle' in book['volumeInfo']:
                #    print(": " + book['volumeInfo']['title'], end='')
                #print()
        #print(response)
        if newestVersionYear > year:
            print(f"Es wurde eine neuere Version von {title} aus dem Jahr {newestVersionYear} gefunden")
        else:
            print(f"Es wurde keine neuere Version von {title} gefunden")
    else:
        print('Fehler beim GET-Request:', response.status_code)


get_book_google("Detterbeck Steffen", "Öffentliches Recht", "2014")
