from scrap import run_query, parse_result
import streamlit as st
import json
import string
import pandas as pd


st.title('Tarkov Buddy')

# item choice
item = st.text_input('Write your item')

with open('bdd/items_db.json', mode='r', encoding='utf-8') as f:
    u_data = json.load(f)  # full dict
data = u_data['data']['items']  # usable list


# method to uniform the name of the items and the input of user
def uniform_item(item):
    punc = string.punctuation
    for p in punc:
        item = item.replace(p, '')
    uni_item = item.lower()
    return uni_item


options = []
for i in data:
    if uniform_item(item) in uniform_item(i['shortName']):  # item_name cleaning
        options.append(i['name'])
    elif uniform_item(item) in uniform_item(i['name']):
        options.append(i['name'])


# User item selection, keep them in session state and clean the Null values
selected_item = st.selectbox('Choose your item', options, index=None)

if 'selected_items' not in st.session_state:
    st.session_state['selected_items'] = []


if selected_item is not None:
    names = [it['name'] for it in st.session_state['selected_items']]
    if selected_item not in names:
        sel_item = next((i for i in data if i["name"] == selected_item), None)
        if sel_item:
            loc_dict = {"id": sel_item['id'], "name": sel_item['name']}
            st.session_state['selected_items'].append(loc_dict)

st.write('You chose', selected_item)


# --- button remove ---
def remove_item(idx):
    del st.session_state['selected_items'][idx]
    st.rerun()  


items_nb = len(st.session_state['selected_items'])
col1, col2 = st.columns([3, 1])

with col1:
    st.header('Item')
    for it in st.session_state['selected_items']:
        st.write(it['name'])

with col2:
    st.header('Remove')
    for i, it in enumerate(st.session_state['selected_items']):
        st.button(
            'Remove',
            key=f"remove_{it['id']}",
            on_click=remove_item,
            args=(i,)
        )

def get_comparison():
    if 'selected_items' not in st.session_state:
        st.session_state['Items to search'] = []
    for s in st.session_state['selected_items']:
        st.session_state['Items to search'].append(s)
    
    responses = run_query(st.session_state['Items to search'])

    pass



st.session_state
