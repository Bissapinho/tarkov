# Tarkov Buddy
Tarkov Buddy is a lightweight Streamlit web application for inspecting and comparing Escape From Tarkov items based on price, size, and value-per-slot efficiency.

---

## Overview
Tarkov Buddy provides users with:

- A searchable local database of all Tarkov items (extracted from the Tarkov.dev GraphQL API)  
- An interactive selection interface  
- A persistent selection state using Streamlit  
- Planned comparison features using live item prices from the API  

This tool is intended for players who want to evaluate what to pick up during raids or analyse stash profitability.

---

## Features

### Current
- Full Tarkov item database
- Interactive search bar with string normalization
- Multi-item selection through Streamlit widgets
- Add/remove selected items without resetting the interface

### Planned
- Cached database loading for faster UI performance  
- Improved UI layout and visual elements  
- Arbitrage trading by detecting anomalies in the marketplace

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourname/tarkov-buddy.git
cd tarkov-buddy
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Update the item database
(Required the first time, recommended after Tarkov patches)

```bash
python itemsbddupdate.py
```

### Run the Streamlit application
```bash
streamlit run app.py
```

This will open the interface in your browser.


## Data Source
Item data originates from the public Tarkov.dev GraphQL API:  
https://api.tarkov.dev/graphql

---

## Contributing
Contributions and suggestions are welcome.  

---

## License
This project is licensed under the MIT License.
