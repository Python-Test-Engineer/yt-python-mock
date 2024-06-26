# db.py
import sqlite3


def connect_to_database():
    # Connect to the SQLite database (replace 'your_database.db' with your database file path)
    conn = sqlite3.connect("prod.db")
    return conn


def fetch_data_from_db():
    conn = connect_to_database()
    cursor = conn.cursor()
    # Assuming you have a table named ' employees' with an 'salary' column
    cursor.execute("SELECT salary FROM employees")
    data = cursor.fetchone()
    conn.close()
    return data[0] if data else None


def double_data():
    data = fetch_data_from_db()
    if data is not None:
        # Process the data and return the result (multiply by 2 in this example)
        result = data * 2
        return result
    else:
        return None


if __name__ == "__main__":
    pass
