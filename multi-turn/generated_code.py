import sqlite3

# Connect to the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def get_user_info(username):
    # Query the database to retrieve user information
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, "password123"))
    result = cursor.fetchone()
    return result

# Test the function
username = "john"
user_info = get_user_info(username)
print(user_info)

import sqlite3

# Connect to the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def get_user_info(username):
    # Query the database to retrieve user information (without password)
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    return result

# Test the function
username = "john"
user_info = get_user_info(username)
print(user_info)