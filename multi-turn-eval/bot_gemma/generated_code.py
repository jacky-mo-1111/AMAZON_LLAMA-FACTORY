def divide(x, y):
    if y == 0:
        raise ZeroDivisionError, "Cannot divide by zero"
    return x / y

def login(username, password):
    try:
        # Database query to check credentials (simplified)
        user = get_user_from_db(username) 
        if user and user["password"] == password:
            return True 
        else:
            raise ValueError("Invalid username or password") 
    except Exception as e:
        print("Login failed:", e) # Broad error handling
        return False

def login(username, password):
    try:
        user = get_user_from_db(username) 
        if not user:
            raise ValueError("Invalid username")
        if user["password"] != password:
            raise ValueError("Invalid password") 
        return True 
    except ValueError as e:
        print(f"Login failed: {e}")  # Specific error message
        return False 
    except DatabaseError as e:
        print(f"Database error during login: {e}") 
        return False

class InvalidInputError(ValueError):
    def __init__(self, message, invalid_value):
        super().__init__(message)
        self.invalid_value = invalid_value

# Usage
try:
    process_data(invalid_input="abc")
except InvalidInputError as e:
    print(f"Invalid input: {e.message}, Value: {e.invalid_value}")

try:
    # Code that might raise an exception
except FileNotFoundError:
    print("File not found, trying a different location...")
except ValueError:
    print("Invalid input provided.")
else:
    print("Operation completed successfully.")
finally:
    # Close files, release connections, etc.

def process_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            for line in f:
                values = line.split(',')
                # Perform calculations ... 
                # ... potential for ValueError if values are not numeric
                result = calculate_something(int(values[0]), float(values[1]))
                with open(output_file, 'a') as o:
                    o.write(str(result) + '\n')
    except Exception as e:
        print("Error processing CSV:", e)

process_csv('data.csv', 'output.csv')

def process_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        for line in f:
            try:
                values = line.split(',')
                result = calculate_something(int(values[0]), float(values[1])) 
                with open(output_file, 'a') as o:
                    o.write(str(result) + '\n')
            except ValueError as e:
                print(f"Error processing line: {line}, Error: {e}")
            except Exception as e:
                print(f"Unexpected error processing line: {line}, Error: {e}")