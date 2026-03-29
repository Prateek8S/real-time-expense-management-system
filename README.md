# <span style="color: #F39C12">Real-time Expense Management System</span>

This is a full-stack application for managing personal or business expenses in real time. The system performs CRUD operations on a MySQL database, exposes a RESTful backend using **FastAPI**, and provides an interactive UI built with **Streamlit**

## How It Works

1. The **backend server** (FastAPI) exposes REST endpoints.
2. The **frontend** (Streamlit) runs separately and sends HTTP requests to the backend.
3. User interacts with the interface to:
   - Fetch existing records : 'GET' request to API
   - Add or delete records : 'POST' request to API
4. The backend executes the corresponding logic and updates the database


## Proof of Work

Check out the working demo of the application:
👉 https://bit.ly/4uTLwEJ


PROJECT STRUCTURE : 
real-time-expense-management-system/
├── backend/
│   ├── db_helper.py
│   ├── logging_setup.py
│   ├── server_logs.log
│   └── server.py
├── frontend/
│   ├── add_update_ui.py
│   ├── analytics_ui.py
│   ├── app.py
│   └── view_only_ui.py
├── tests/
│   ├── backend_tests/
│       └── test_db_helper.py
│   ├── frontend_tests/
│   └── conftest.py
├── .env
└── requirements.txt



