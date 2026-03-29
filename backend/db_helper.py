## Purpose of this file: This file contains helper functions to interact with the database, retrieve, insert, update, and delete expense records.
## This is called CRUD - Create, Read, Update, Delete operations.

# pip install mysql-connector-python
import os
import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger
from dotenv import load_dotenv
load_dotenv()


logger = setup_logger("db_helper")

@contextmanager
def get_db_cursor(commit=False):
    ## Establishing the connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database="expense_manager"
    )

    if connection.is_connected():
        print("Successfully connected to the database...")
    else:
        print("Connection to the database failed!")
    
    ## Creating a cursor object to interact with the database
    cursor = connection.cursor(dictionary=True)
    yield cursor   ### ---------> Returns the connection and cursor and the object variables still remain in scope.
    
    ## Committing changes if needed
    if commit:
        connection.commit()
        print("\nChanges committed to the database ...\n")
    
    ## FInally closing the cursor and connection
    cursor.close()
    connection.close()
    
    
    
## --------------------------------------------------------------------------------------------------------------------------------------
## --------------------------------------------------------------------------------------------------------------------------------------
## CRUD Operations


def fetch_all_records():
    with get_db_cursor() as cursor:      ## --------------------> (yeild cursor)
        """ When we go outside the 'with' statement, the context manager moves next to see 'if commit' and then moves next to automatically close the cursor and connection. """
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
       
       
       
def insert_expenses(expense_date, amount, category, notes):
    logger.info(f"Function insert_expenses called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        ## Inserting a new expense record
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )
        print("\nExpense record staged successfully!")



def fetch_expenses_for_date(date):
    logger.info(f"Function fetch_expenses_for_date called with date: {date}")
    with get_db_cursor() as cursor:
    ## Fetching records for a specific date
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
        return expenses
     
     
    
def delete_expenses_for_date(date):
    logger.info(f"Function delete_expenses_for_date called with date: {date}")
    with get_db_cursor(commit=True) as cursor:
    ## Deleting records for a specific date
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (date,))
        print(f"\nRemoval of expenses for date {date} is staged ...")
        
        
        
def fetch_expenses_summary(start_date, end_date):
    logger.info(f"Function fetch_expenses_summary called with start_date: {start_date}, end_date: {end_date}")
    with get_db_cursor() as cursor:
    ## Fetching summary of expenses between two dates
        cursor.execute(
            "SELECT category, SUM(amount) as total_amount FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category",
            (start_date, end_date)
        )
        data = cursor.fetchall()
        # for record in data:
        #     print(record)
        return data

        
        
if __name__ == "__main__":
    expenses = fetch_expenses_for_date("2024-08-15")
    # print(expenses)
    
    # insert_expenses("2024-08-25", 80, "Food", "Samosa and tea")
    
    # delete_expenses_for_date("2024-08-25")
    
    summary = fetch_expenses_summary("2024-08-01", "2024-08-05")
    for record in summary:
        print(record)
    

