from scrap import run_query, parse_result
import streamlit as st
import json
import string
import pandas as pd


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


options = []
for i in data:
    if uniform_item(item) in uniform_item(i['shortName']): #item_name cleaning
        options.append(i['name'])
    elif uniform_item(item) in uniform_item(i['name']):
        options.append(i['name'])


#User item selection, keep them in session state and clean the Null values
selected_item = st.selectbox('Choose your item', options, index = None)
if 'selected_items' not in st.session_state:
    st.session_state['selected_items'] = []

if selected_item not in st.session_state['selected_items'] and selected_item is not None: 
    st.session_state['selected_items'].append(selected_item)

st.write('You chose', selected_item)

#dataframe creation with the item with a button remove
def remove_item(i):
    del st.session_state['selected_items'][i]
    pass

items_nb = len(st.session_state['selected_items'])
col1, col2 = st.columns(2)

with col1:
    st.header('Item')
    for _ in range(items_nb):
        st.session_state['selected_items'][_]

with col2:
    st.header('Remove')
    for _ in range(items_nb):
        st.button('Remove', key = _)


st.session_state

#whats next
#configurer le on_click des boutons et ajuster les largeurs des lignes (alignement)
#Mieux traiter l'import de la bdd et la foutre en cache streamlit
#faire la comparaison == MVP fonctionnelle
#ameliorer la barre de recherche (plus tard)
#tej toutes les fonctions de ce fichier et les mettre dans d'autres fichier pour clean app.py
