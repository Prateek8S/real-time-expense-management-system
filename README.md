# <span style="color: #F39C12">Real-time Expense Management System</span>

This is a full-stack application for managing personal or business expenses in real time. The system performs CRUD operations on a MySQL database, exposes a RESTful backend using **FastAPI**, and provides an interactive UI built with **Streamlit**


## How It Works

1. The **backend server** (FastAPI) exposes REST endpoints.
2. The **frontend** (Streamlit) runs separately and sends HTTP requests to the backend.
3. User interacts with the interface to:
   - Fetch existing records : 'GET' request to API
   - Add or delete records : 'POST' request to API
4. The backend executes the corresponding logic and updates the database




Application demonstration : https://bit.ly/4uTLwEJ




