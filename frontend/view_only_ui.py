import streamlit as st
from datetime import datetime
import pandas as pd
import requests
import json


API_URL = "http://127.0.0.1:8000"

def view_only_tab():

    view_date = st.date_input("Select Date to View Expenses", value=datetime(2024, 8, 1), key="view_date_selector")

    response = requests.get(f"{API_URL}/expenses/{view_date}")
    
    if response.status_code == 200:
        existing_expenses = response.json()
        
        if not existing_expenses:
            st.info(f"No expense records found for **{view_date.strftime('%Y-%m-%d')}**.")
        else:
            st.success(f"Found **{len(existing_expenses)}** expense(s) on **{view_date.strftime('%Y-%m-%d')}**")

            df = pd.DataFrame(existing_expenses)
            
            df["amount"] = df["amount"].apply(lambda x: f"$ {x:,.2f}")
            
            df["notes"] = df["notes"].fillna("_(no notes)_").replace("", "_(no notes)_")

            st.table(df)

            st.download_button(
                "Download as JSON",
                data=json.dumps(existing_expenses, indent=2),
                file_name=f"expenses_{view_date}.json",
                mime="application/json"
            )
            

    else:
        st.error("Failed to fetch expense records. Please try again later.")