import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=()):
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        # Open the connection
        self.connection = sqlite3.connect("my_database.db")
        self.cursor = self.connection.cursor()

        # Execute a query with parameters
        self.cursor.execute(self.query, self.params)

        # get result
        self.results = self.cursor.fetchall()

        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the connection and save changes
        if self.connection:
            self.connection.commit()
            self.connection.close()

if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery(query, params) as results:
        for row in results:
            print(row)
