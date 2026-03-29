# <span style="color: #F39C12">Real-time Expense Management System</span>

This is a full-stack application for managing personal or business expenses in real time. The system performs CRUD operations on a MySQL database, exposes a RESTful backend using **FastAPI**, and provides an interactive UI built with **Streamlit**


## How It Works

The application follows a simple yet effective client-server architecture:

1. The frontend runs independently and and communicates with the backend server via HTTP requests.
2. Users interact with the intuitive Streamlit interface to perform the following actions:
   - View expenses → Sends a GET request to fetch existing records
   - Add new expenses → Sends a POST request to create records
   - Delete expenses → Sends a POST/DELETE request to remove records
3. The backend server receives and processes each request, executes the corresponding business logic, interacts with the MySQL database, and returns the appropriate response to the frontend.
4. Changes are reflected immediately in the interface, providing a smooth real-time expense tracking experience.




Application demonstration : https://bit.ly/4uTLwEJ




