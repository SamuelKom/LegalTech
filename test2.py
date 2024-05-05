import requests
import json

project_id = "elite-coral-422320-q3"

# URL of the API endpoint
url = "https://us-central1-aiplatform.googleapis.com/v1/projects/" + project_id + "/locations/us-central1/publishers/google/models/text-bison:predict"

prompt = "extract author, title and year from: Detterbeck, Steffen: Öffentliches Recht – Ein Basislehrbuch zum Staatsrecht, Verwaltungsrecht und Europarecht mit Übungsfällen, 11. Auflage, München 2018, zitiert als: Detterbeck, Basislehrbuch, § Rn."


# Data to be sent in JSON format
data = {
  "instances": [
    { 
        "prompt": prompt   
    }
  ],
  "parameters": {
    "temperature": 1,
    "maxOutputTokens": 1024,
    "topP": 1
  }
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Authorization token (assume you have a valid token)
#./google-cloud-sdk/bin/gcloud auth print-access-token
token = "ya29.a0AXooCgv8l_67cQRCvlpS65PkC6SL_S0h45zM7wr-0C0uYEJbQaznHdP6rwX1Lyf9kQgmEFo7nwLSHa3C1paP16oNAlbjHghmmtDJ6SRLv-FLUNFApqdyFEw2WeI-6ZL2UMMnOiNXw-pGMP3kgG4as9e8DuNrOXLcSwC1WwzMIQaCgYKAVASARISFQHGX2Mi8uCK8e50ymQGtH18eWyrDA0177"

# Headers including the Content-Type and Authorization
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

# Make the POST request with the JSON body and headers
response = requests.post(url, data=json_data, headers=headers)

# Print the status code and response data
print("Status Code:", response.status_code)
print("Response:", response.json())
