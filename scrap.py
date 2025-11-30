import requests
import pandas as pd 


def run_query(items):

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



def parse_result(result):
    info = []

    for r in result:
        items = r.get("data", {}).get("items", [])
        if not items:
            continue

        data = items[0]

        # width/height safety
        width = data.get("width", 1) or 1
        height = data.get("height", 1) or 1
        size = float(width) * float(height)

        # price safety
        avg_price = data.get("avg24hPrice")
        if avg_price is None:
            avg_price = 0

        value_per_sq = avg_price / size

        local_info = {
            "Name": data.get("name", "Unknown"),
            "value per squares": value_per_sq,
            "Image": data.get("imageLink", ""),
        }

        info.append(local_info)

    df = pd.DataFrame(data=info)
    df = df.sort_values(by=['value per squares'], ascending=False)
    return df




