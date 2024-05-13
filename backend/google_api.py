import requests
import os

#from dotenv import load_dotenv

#load_dotenv('.env') 

#ISBN_DB_API_KEY = os.environ.get('ISBN_DB_API_KEY')

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"
#ISBN_DB_API_URL = "https://api2.isbndb.com/books/"

def get_book_google(author, title, year: int):
    #payload = {'column': 'title'}
    #headers = {'Authorization': 'application/json'}
    params = {
        "q": f'intitle:{title} inauthor:{author}'
    }
    response = requests.get(GOOGLE_BOOKS_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        newestVersionYear = year
        for book in data['items']:
            print(f"{author}, {title}")
            if 'volumeInfo' in book:
                volumeInfo = book['volumeInfo']
                if 'title' in volumeInfo and 'publishedDate' in volumeInfo and 'authors' in volumeInfo:
                    volumeYear = int(volumeInfo['publishedDate'].split("-")[0])
                    print(volumeYear, ", ", newestVersionYear)

                    if volumeYear > newestVersionYear:
                        newestVersionYear = volumeYear
        if newestVersionYear > year:
            return (f"Es wurde eine neuere Version gefunden")
        else:
            return (f"Es wurde keine neuere Version gefunden")
    else:
        print('Fehler beim GET-Request:', response.status_code)


#get_book_google("Detterbeck Steffen", "Öffentliches Recht", "2014")
