import pytest
import datetime
from backend import db_helper



def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")
    
    assert isinstance(expenses, list)
    
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes'] == "Bought potatoes"
    assert expenses[0]['expense_date'] == datetime.date(2024, 8, 15)
    
    
    
    
def test_fetch_expenses_for_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")
    assert len(expenses) == 0
    
    
    

def test_insert_and_delete_expenses():
    test_date = "2024-08-28"
    db_helper.insert_expenses(test_date, 50.0, "Entertainment", "Movie tickets")
    
    expenses = db_helper.fetch_expenses_for_date(test_date)
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 50.0
    assert expenses[0]['category'] == "Entertainment"
    assert expenses[0]['notes'] == "Movie tickets"
    assert expenses[0]['expense_date'] == datetime.date(2024, 8, 28)
    
    db_helper.delete_expenses_for_date(test_date)
    
    expenses_after_deletion = db_helper.fetch_expenses_for_date(test_date)
    assert len(expenses_after_deletion) == 0