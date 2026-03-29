from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper

## Defining response schema :
class ExpenseRecord(BaseModel):
    # expense_date: date
    amount: float
    category: str
    notes: str
    
## Defining date range schema for analytics
class DateRange(BaseModel):
    start_date: date
    end_date: date


app = FastAPI()

## fetch expense records for a specific date
@app.get("/expenses/{expense_date}", response_model=List[ExpenseRecord])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses for the given date")
    
    return expenses
    # return f"Retrieving get_expenses request for date: {expense_date}"
    
    
## insert a new expense record
@app.post("/expenses/{expense_date}")
def update_new_expense(expense_date: date, expenses: List[ExpenseRecord]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expenses(
            expense_date, expense.amount, expense.category, expense.notes
            )
    return {"message": "New records updated"}



## Get analytics summary between two dates
@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expenses_summary(date_range.start_date, date_range.end_date)
    
    if data is None:
        raise HTTPException(status_code=500, detail="No data found for the given date range")
    
    # total = 0
    # for row in data:
    #     total += row['total_amount']
    
    total = sum([row['total_amount'] for row in data])   ## ---------> List comprehension way: An Alternative
    
    breakdown = {}
    ## Calculate percentage
    for row in data:
        percentage = (row['total_amount'] / total) * 100 if total != 0 else 0
        percentage = round(percentage, 2)
        
        breakdown[row['category']] = {
            'total_amount': row['total_amount'],
            'percentage': percentage
        }
        
    return breakdown

        

  
    








