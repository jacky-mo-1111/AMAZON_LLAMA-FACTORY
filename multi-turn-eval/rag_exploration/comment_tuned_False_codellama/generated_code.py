def fetch_records(search_name, cursor):
    query = f"SELECT * FROM employees WHERE name = '{search_name}'"
    cursor.execute(query)
    return cursor.fetchall()

employee_records = fetch_records('John Doe', cursor)

def connect_to_db(db_path):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        return connection, cursor
    except Exception as error:
        print(f"Unable to connect to database: {error}")
        return None, None

def main():
    try:
        conn, cursor = connect_to_db('company.db')
        employee_records = fetch_records('John Doe', cursor)
        transformed_records = transform_data(employee_records)
        print("Employee Names:", transformed_records)
        conn.close()
    except Exception as error:
        print(f"Unable to execute program: {error}")

records = [
    [0, 'John Doe'],
    [1, 'Jane Doe'],
    [2, 'Bob Smith'],
]

def transform_data(records):
    transformed = [record[1].upper() for record in records]
    return transformed