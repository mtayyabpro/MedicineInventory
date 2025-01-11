import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',  # Use your MySQL password here
            database='inventory_management'
        )
        if conn.is_connected():
            cursor = conn.cursor()  # Create the cursor
            print("Connection to the database established successfully.")
            return conn, cursor    # Return both connection and cursor
    except Error as e:
        print(f"Error: {e}")
        return None, None  # Return None for both if connection fails

# Close the connection and cursor
def close_connection(conn, cursor):
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Connection closed successfully.")
    except Error as e:
        print(f"Error closing connection: {e}")
