# Flask API Documentation

## Getting Started

To use this API, follow the steps below:

1. Clone the repository:
   ```
   git clone this url
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the Flask application:
   ```
   python app.py
   ```

## Authentication

To access protected endpoints, you need to log in using the following credentials:
- **Username:** Any username
- **Password:** 123456

After logging in, you will receive a token. Copy this token and use it as a query parameter for protected endpoints.

## Endpoints

### 1. Home Page
- **URL:** `/`
- **Methods:** GET, POST

The home page allows you to log in to the application. If you are already logged in, you will be redirected to the home page.

### 2. Get All Users
- **URL:** `/user`
- **Method:** GET
- **Authentication:** Required (Token)
- **Description:** Retrieves a list of all users in the database.

### 3. Add User
- **URL:** `/add_user`
- **Method:** POST
- **Authentication:** Required (Token)
- **Description:** Adds a new user to the database.

   **Request Parameters:**
   - `name` (string, required): The name of the user to be added.

   **Response:**
   - Successful Response (HTTP Status Code 201):
     ```json
     {
       "message": "User added successfully",
       "name": "<user_name>"
     }
     ```
   - Error Response (HTTP Status Code 400):
     ```json
     {
       "message": "Name parameter is missing or empty"
     }
     ```
     OR
     - Error Response (HTTP Status Code 500):
       ```json
       {
         "message": "Error occurred while adding the user",
         "error": "<error_message>"
       }
       ```

### 4. Login
- **URL:** `/login`
- **Method:** POST
- **Description:** Logs in a user and provides an authentication token.

   **Request Parameters:**
   - `username` (string, required): The username for authentication.
   - `password` (string, required): The password for authentication (must be '123456').

   **Response:**
   - Successful Response (HTTP Status Code 200):
     ```json
     {
       "token": "<authentication_token>",
       "info": {
         "token": {
           "user": "<username>",
           "expiration": "<expiration_timestamp>"
         }
       }
     }
     ```
   - Error Response (HTTP Status Code 403):
     ```
     Unable to verify
     ```

### 5. Logout
- **URL:** `/logout`
- **Method:** GET
- **Description:** Logs out the currently logged-in user.

   **Response:**
   ```
   logout successful
   ```
  