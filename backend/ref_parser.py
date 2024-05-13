from typing import List
import requests
import json
from datetime import datetime, timedelta
import subprocess

from structure import ParseInfo

#curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-474.0.0-linux-x86_64.tar.gz
#tar -xf google-cloud-cli-474.0.0-linux-x86_64.tar.gz
#./google-cloud-sdk/install.sh
#./google-cloud-sdk/bin/gcloud init
#./google-cloud-sdk/bin/gcloud components install gsutil bq
#sudo snap install google-cloud-sdk

class Parser:
    def __init__(self) -> None:
        self.project_id = "elite-coral-422320-q3"
        self.url = "https://us-central1-aiplatform.googleapis.com/v1/projects/" + self.project_id + "/locations/us-central1/publishers/google/models/text-bison:predict"
        self.basic_request = "extract author, title and year from: "
        self.token = None
        self.request_token_time = None

    def get_new_token(self) -> None:
        self.request_token_time = datetime.now()

        #command = "./google-cloud-sdk/bin/gcloud auth print-access-token".split(" ")
        #p =  subprocess.Popen(command, stdout=subprocess.PIPE) #, shell=True, text=True)
        #(output, err) = p.communicate()
        #self.token = output.decode('utf-8')
        self.token = "ya29.a0AXooCgtke3s-7nGDgtcG8YIsvCrs6W_x35VlMS5UBoqs9dwFDFVaNaqjMTDJjW4fUK5ku2vImyg-z1oiNomi8SEwI6ZWI_khbreliz6NyVNi32jIoRjekMjvLTJaiO2BifsBxDcBIwTG6VogwZipoCI9qzBJ2H6bClRaMKpBty0aCgYKAWkSARISFQHGX2MipS_Xwkt0izabg8pdAzp7GA0178"

    def split_sources(self, msg: str) -> List[str]:
        raise NotImplementedError
    
    def __send_request(self, book) -> dict:
        json_data = json.dumps({
            "instances": [
                { 
                    "prompt": self.basic_request + book
                }
            ],
            "parameters": {
                "temperature": 1,
                "maxOutputTokens": 1024,
                "topP": 1
            }
        })
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(self.url, data=json_data, headers=headers)
        #print("Status Code:", response.status_code)
        #print("Response:", response.json())
        return response.json()

    
    def get_data_obj(self, book: str) -> ParseInfo:
        if self.request_token_time == None or datetime.now() + timedelta(minutes=10) > self.request_token_time:
            self.get_new_token()

        response = self.__send_request(book)
        response = response["predictions"][0]["content"]
        #title_value = ""
        #year_value = 0
        #author_value = ""
        for attribute in response.split("\n"):
            attribute_cleaned = attribute.strip()
            #print(response)
            if attribute_cleaned.startswith('Title:'):
                title_value = attribute_cleaned.split(':', 1)[1].strip()
            elif attribute_cleaned.startswith('Year:'):
                year_value = attribute_cleaned.split(':', 1)[1].strip()
            if attribute.strip().startswith('Author:'):
                author_value = attribute.split(':', 1)[1].strip()
        return ParseInfo(title=title_value, author=author_value, year=int(year_value))
