Tarkov Buddy

Tarkov Buddy is a lightweight Streamlit web application for inspecting and comparing Escape From Tarkov items based on price, size, and value-per-slot efficiency.

Overview

Tarkov Buddy provides users with:

A searchable local database of all Tarkov items (extracted from the Tarkov.dev GraphQL API)

An interactive selection interface

A persistent selection state using Streamlit

Planned comparison features using live item prices from the API

This tool is intended for players who want to evaluate what to pick up during raids or analyse stash profitability.

Features
Current

Full Tarkov item database stored locally in items_db.json

Interactive search bar with string normalization

Multi-item selection through Streamlit widgets

State persistence via st.session_state

Add/remove selected items without resetting the interface

Planned

Value-per-slot comparison:

Fetching live price data from Tarkov.dev

Computing value per square (avg24hPrice / total slots)

Producing a sorted comparison DataFrame

Cached database loading for faster UI performance

Improved UI layout and visual elements

Installation

Clone the repository:

git clone https://github.com/yourname/tarkov-buddy.git
cd tarkov-buddy


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows


Install dependencies:

pip install -r requirements.txt

Usage
Update the item database

(Optional, recommended after Tarkov patches)

python itemsbddupdate.py

Run the Streamlit application
streamlit run app.py


This will open the interface in your browser.
