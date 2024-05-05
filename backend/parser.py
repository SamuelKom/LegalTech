from typing import List
import re
import requests
import json
import numpy
import spacy
import random
from copy import deepcopy

from backend.structure import ParseInfo

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
        self.token = "ya29.a0AXooCgv8l_67cQRCvlpS65PkC6SL_S0h45zM7wr-0C0uYEJbQaznHdP6rwX1Lyf9kQgmEFo7nwLSHa3C1paP16oNAlbjHghmmtDJ6SRLv-FLUNFApqdyFEw2WeI-6ZL2UMMnOiNXw-pGMP3kgG4as9e8DuNrOXLcSwC1WwzMIQaCgYKAVASARISFQHGX2Mi8uCK8e50ymQGtH18eWyrDA0177"

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
        print("Status Code:", response.status_code)
        print("Response:", response.json())
        return response.json()

    
    def get_data_obj(self, book: str, delimiters: List[str]) -> ParseInfo:
        response = self.__send_request(book)
        response = response["predictions"][0]["content"]
        for attribute in response.split("\n"):
            attribute_cleaned = attribute.strip()
            if attribute_cleaned.startswith('Title:'):
                title_value = attribute_cleaned.split(':', 1)[1].strip()
            elif attribute_cleaned.startswith('Year:'):
                year_value = attribute_cleaned.split(':', 1)[1].strip()
            if attribute.strip().startswith('Author:'):
                author_value = attribute.split(':', 1)[1].strip()
        print(response)
        return ParseInfo(title=title_value, author=author_value, year=int(year_value))
