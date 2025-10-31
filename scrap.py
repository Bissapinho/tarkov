import requests
import pandas as pd 


items = ["AS VAL 9x39 special assault rifle Default",
         "ASh-12 12.7x55 assault rifle Default",
         "B&T MP9 9x19 submachine gun Default",
         "B&T MP9-N 9x19 submachine gun Default",
         "20x1mm toy gun Default"]


def run_query():
    
    global items #temporary, use tkinter interface later
    responses = []
    headers = {"Content-Type": "application/json"}

    for item in items:
        new_query = f"""
    {{
      items(lang: en, name: "{item}") {{
        id
        name
        avg24hPrice
        basePrice
        low24hPrice
        width
        imageLink
        lastOfferCount
        height
      }}
    }}
    """    
        response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': new_query})
        if response.status_code == 200:
            responses.append(response.json())
        else:
            continue
    return responses


result = run_query()
print(result)

def parse_result(result):
    info = []
    for r in result:
        local_info = {}
        items = r.get("data", {}).get("items", [])
        if not items:
            continue 

        data = items[0]
        size = float(data['width']) * float(data['height']) or 1 #will prevent division by 0 if any pb occur
        avg_price = data['avg24hPrice']
        value_per_sq = avg_price / size

        #Add info of the iterated item to the locl dict

        local_info = {
    "Name": data["name"],
    "value per squares": value_per_sq,
    "Image": data["imageLink"]
    }

        info.append(local_info) #adding to the global list the info about the local item
    
    df = pd.DataFrame(data = info)
    df = df.sort_values(by=['value per squares'], ascending = False)
    return df

print(parse_result(result))


