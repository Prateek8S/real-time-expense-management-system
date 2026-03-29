# <span style="color: #F39C12">Real-time Expense Management System</span>

This is a full-stack application for managing personal or business expenses in real time. The system performs CRUD operations on a MySQL database, exposes a RESTful backend using **FastAPI**, and provides an interactive UI built with **Streamlit**


## How It Works

1. The frontend runs independently and sends HTTP requests to the backend server.
2. Users interact with the intuitive Streamlit interface to perform the following actions:
   - View expenses → Sends a GET request to fetch existing records
   - Add new expenses → Sends a POST request to create records
   - Delete expenses → Sends a POST/DELETE request to remove records
3. The FastAPI backend receives the requests, executes the corresponding business logic, interacts with the MySQL database, and returns the appropriate response to the frontend.
4. The updated data is instantly reflected in the Streamlit UI, enabling real-time expense tracking.




Application demonstration : https://bit.ly/4uTLwEJ




