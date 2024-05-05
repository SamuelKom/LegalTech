import requests
import os
from dotenv import load_dotenv

load_dotenv('.env') 
ISBN_DB_API_KEY = os.environ.get('ISBN_DB_API_KEY')
ISBN_DB_API_URL = "https://api2.isbndb.com"
header = {"Authorization": ISBN_DB_API_KEY}

# def is_book(author, title):
response = requests.get(ISBN_DB_API_URL + "/books/" + "Das private „Hausrecht“", headers=header)

data = response.json()
if data.get("errorMessage") == "Not Found":
    print("Not a book")
else: 
    print("Is a book")