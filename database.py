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
        return conn
    except Error as e:
        return None
