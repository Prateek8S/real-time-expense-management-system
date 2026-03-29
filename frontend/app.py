from add_update_ui import add_update_tab
from view_only_ui import view_only_tab
from analytics_ui import analytics_tab
import streamlit as st
from datetime import datetime
import requests


API_URL = "http://127.0.0.1:8000"

st.title("Expense Management System")

tab_view, tab_update, tab_analytics = st.tabs(["View Expenses", "Add / Update Expense", "Analytics"])


with tab_view:
    view_only_tab()
    

with tab_update:
    add_update_tab()
    
    
with tab_analytics:
    analytics_tab()
    
                
            
    






# expense_dt = st.date_input("Expense Date: ")
# if expense_dt:
#     st.write(f"Fetching expenses for {expense_dt}")
    