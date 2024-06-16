# Leaf Colour Quantifier - Backend

Welcome to the backend repository of the Leaf Colour Quantifier project. This backend serves as the API for the Leaf Colour Quantifier, providing image processing and analysis capabilities.

## Setup

Follow these steps to set up the backend environment:

1. Clone the Repository:

   ```bash
   cd backend
   ```

2. Create a Virtual Environment (Optional but Recommended):

   ```bash
   python -m venv env
   ```

3. Activate the Virtual Environment:

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source env/bin/activate
     ```

4. Install Required Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Backend

To run the backend server, use the following commands:

1. Change to the `backend` directory if you're not already there:

   ```bash
   cd backend
   ```

2. Activate the Virtual Environment (if not already activated):

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source env/bin/activate
     ```

3. Start the FastAPI Application:

   ```bash
   python main.py
   ```

The backend server will start, and you will see output indicating the server is running. By default, the server will be accessible at `http://localhost:5000`.

## API Documentation

- http://localhost:5000/docs

  - Access the interactive Swagger documentation for the API.

- http://localhost:5000/openapi.json

  - Download the OpenAPI JSON file to use with your API client.

- http://localhost:5000/redoc
  - View API documentation in a user-friendly ReDoc interface.
