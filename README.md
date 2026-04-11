# Real-Time Expense Management System

A full-stack application for tracking personal or business expenses in real time. Built with **FastAPI** on the backend, **Streamlit** on the frontend, and **MySQL** as the data store.

---

## Table of Contents

- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Frontend Features](#frontend-features)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Screenshots](#screenshots)

---

## Architecture

The application follows a three-tier client-server architecture:

1. Users interact with the Streamlit interface to view, add, update, or delete expenses.
2. Each action triggers an HTTP request (GET or POST) to the FastAPI backend.
3. The backend processes the request, executes the corresponding database operation via MySQL, and returns the response.
4. Changes are reflected immediately in the UI, providing a smooth real-time experience.

---

## Project Structure

```
real-time-expense-management-system/
│
├── backend/
│   ├── server.py            # FastAPI app — defines API endpoints and Pydantic models
│   ├── db_helper.py         # Database CRUD operations using mysql-connector-python
│   ├── logging_setup.py     # Centralized logger configuration
│   └── server_logs.log      # Runtime log output
│
├── frontend/
│   ├── app.py               # Streamlit entry point — sets up the tabbed interface
│   ├── view_only_ui.py      # "View Expenses" tab — fetch and display records
│   ├── add_update_ui.py     # "Add / Update Expense" tab — form-based CRUD
│   └── analytics_ui.py      # "Analytics" tab — date-range summaries and charts
│
├── tests/
│   ├── conftest.py          # Pytest path configuration
│   └── backend_tests/
│       └── test_db_helper.py  # Unit tests for database helper functions
│
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (DB credentials)
└── README.md
```

---

## Tech Stack

- Frontend: Streamlit, Pandas
- Backend: FastAPI, Uvicorn, Pydantic
- Database: MySQL  
- Testing: Pytest  
- Logging: Python `logging` module

---

## Database Schema

The application uses a single MySQL database called `expense_manager` with one table:

### `expenses`

| Column         | Type    | Description                        |
|----------------|---------|------------------------------------|
| `expense_date` | DATE    | Date the expense was incurred      |
| `amount`       | FLOAT   | Monetary value of the expense      |
| `category`     | VARCHAR | One of: Rent, Food, Shopping, Entertainment, Other |
| `notes`        | VARCHAR | Optional description of the expense|

---

## API Endpoints

The FastAPI server runs at `http://127.0.0.1:8000`.

### `GET /expenses/{expense_date}`

Fetch all expense records for a given date.

**Response:** `List[ExpenseRecord]` — each containing `amount`, `category`, and `notes`.

### `POST /expenses/{expense_date}`

Create or update expenses for a given date. Replaces all existing records for that date with the new payload.

**Request Body:** `List[ExpenseRecord]`

**Response:** `{"message": "New records updated"}`

### `POST /analytics/`

Retrieve a category-wise spending summary for a date range.

**Request Body:** `{"start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"}`

**Response:** A dictionary keyed by category, each with `total_amount` and `percentage`.

---

## Frontend Features

The Streamlit UI is organized into three tabs:

### View Expenses
- Pick a date to fetch all recorded expenses.
- Results are displayed in a formatted table with currency formatting.
- Download the data as a JSON file.

### Add / Update Expenses
- Select a date and enter up to 6 expense rows (amount, category, notes).
- The form auto-populates with any existing records for the selected date.
- Submitting replaces the day's records with the updated entries.

### Analytics
- Choose a start and end date to analyze spending patterns.
- View a bar chart showing the percentage breakdown by category.
- A summary table displays totals and percentages, sorted by highest spend.

---

## Getting Started

### Prerequisites

- Python 3.11+
- MySQL Server running locally

### 1. Clone the repository

```bash
git clone https://github.com/Prateek8S/real-time-expense-management-system.git
cd real-time-expense-management-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the database

Create the MySQL database and table:

```sql
CREATE DATABASE expense_manager;

USE expense_manager;

CREATE TABLE expenses (
    expense_date DATE,
    amount       FLOAT,
    category     VARCHAR(255),
    notes        VARCHAR(255)
);
```

### 4. Configure environment variables

Update the `.env` file in the project root with your MySQL credentials:

```
USER = "root"
PASSWORD = "your_password"
```

### 5. Start the backend

```bash
cd backend
uvicorn server:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Visit `http://127.0.0.1:8000/docs` for the interactive Swagger documentation.

### 6. Start the frontend

In a separate terminal:

```bash
cd frontend
streamlit run app.py
```

The Streamlit app will open in your browser, typically at `http://localhost:8501`.

---

## Running Tests

The test suite validates the database helper functions against a live MySQL instance.

```bash
pytest tests/
```

Tests cover fetching expenses for valid and invalid dates, as well as insert and delete operations.


## Demonstration

> Visit the following link to see how the application works : https://bit.ly/4uTLwEJ


---
---


## License

This project is open source and available under the [MIT License](LICENSE).
