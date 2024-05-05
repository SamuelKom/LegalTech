import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.google.com/search?q="
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

def get_links(query):

    url = BASE_URL + query
    data = requests.get(url, headers=header)

    if data.status_code == 200:
        soup = BeautifulSoup(data.content, "html.parser")
        results = []
        for g in soup.find_all('div',  {'class':'g'}):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                try:
                    description = g.find('div', {'data-sncf':'2'}).text
                except Exception as e:
                    description = "-"
                # results.append(str(title)+";"+str(link)+';'+str(description))
                results.append(str(link))
        return results