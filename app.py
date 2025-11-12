from scrap import run_query, parse_result
import streamlit as st
import json
import string


st.title('Tarkov Buddy')

#item choice
item = st.text_input('Write your item')

with open('bdd/items_db.json', mode='r', encoding='utf-8') as f:
    u_data = json.load(f) #full dict
data = u_data['data']['items'] #usable list


#method to uniform the name of the items and the input of user
def uniform_item(item):
    punc = string.punctuation
    for p in punc:
        item = item.replace(p, '')
    uni_item = item.lower()

    return uni_item

#to move later to another file
#add items from teh search bar to a list of items on which the query will be run
def add_item(item):
    global items
    items.append(item)
    return items

options = []
for i in data:
    if uniform_item(item) in uniform_item(i['shortName']): #item_name cleaning
        options.append(i['name'])
    elif uniform_item(item) in uniform_item(i['name']):
        options.append(i['name'])


items = []
selected_item = st.selectbox('Choose your item', options)
st.write('You chose', selected_item)


#whats next
#ajouter un bouton en dessous de select box pour l'ajouter a une 'bdd' temporaire pour ensuite comparer tous les items choisis
#Mieux traiter l'import de la bdd et la foutre en cache streamlit
#faire la comparaison == MVP fonctionnelle
#ameliorer la barre de recherche (plus tard)
#tej toutes les fonctions de ce fichier et les mettre dans d'autres fichier pour clean app.py
