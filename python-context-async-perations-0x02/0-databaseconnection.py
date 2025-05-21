import sqlite3  # For example, we use SQLite for ease of example, you can change it to any other database

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        # Open database connection
        self.connection = sqlite3.connect(self.db_name)
        return self.connection.cursor()  # We will return the cursor to use it for inquiries.

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the connection to the base whether an error occurred or not.
        if self.connection:
            self.connection.commit()  # We will delete any changes before closing.
            self.connection.close()


if __name__ == "__main__":
    with DatabaseConnection("my_database.db") as cursor:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
