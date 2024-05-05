import requests
from bs4 import BeautifulSoup
import re
import scrape

regex = "\d+\. Auflage"

def find_latest_edition(url):
  
    response = requests.get(url)
    content = response.text

    match = re.search(regex, content)
    print(match)


# Sample list of URLs (replace with your actual URLs)
urls = scrape.get_links("Grundgesetz für die Bundesrepublik Deutschland – Kommentar")

find_latest_edition(urls[1])
