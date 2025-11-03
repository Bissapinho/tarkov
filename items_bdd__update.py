import json
import requests

#Short code to update the database of all tarkov items available
#Run this file at every patch

headers = {"Content-Type": "application/json"}

query = """{
  items(lang: en) {
    id
    name
    shortName
    basePrice
    width
    height
    iconLink
  }
}"""

response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
if response.status_code == 200:
    with open('bdd/items_db.json', mode='w', encoding='utf-8') as f:
        json.dump(response.json(), f, indent=4)
else:
    print('Fail')
    
