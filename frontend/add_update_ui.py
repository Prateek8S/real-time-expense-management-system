import streamlit as st
from datetime import datetime
import requests


API_URL = "http://127.0.0.1:8000"

def add_update_tab():
    selected_date = st.date_input("Enter Expense Date ", datetime(2024,8,1), label_visibility="collapsed", key="date_selector")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
        # st.write(existing_expenses)
    else:
        st.error("Failed to retrieve existing expenses")
        existing_expenses = []
        
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")
        

        expenses_input = []
        date_str = selected_date.strftime("%Y-%m-%d")
        
        for i in range(6):  ## Allowing user to input up to 6 expense records at a time
            
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
                
            else:
                amount = 0.0
                category = "Other"  ## Default category
                notes = ""
                
                
                
            col1, col2, col3 = st.columns(3)
            
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}_{date_str}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index = categories.index(category), key=f"category_{i}_{date_str}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}_{date_str}", label_visibility="collapsed")
                
            expenses_input.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })
            
        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses_input if expense['amount'] > 0]

            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error("Failed to update expenses.")