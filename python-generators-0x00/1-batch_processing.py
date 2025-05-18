#!/usr/bin/python3
import mysql.connector
import sys
from contextlib import contextmanager

@contextmanager
def database_connection():
    """Context manager for database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password",
            database="ALX_prodev"
        )
        yield connection
    finally:
        if connection:
            connection.close()

def stream_users_in_batches(batch_size):
    """Yields rows in batches from the database."""
    with database_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM user_data")
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    return  # Explicit return to end generator
                yield batch
        finally:
            cursor.close()

def batch_processing(batch_size):
    """Processes each batch and prints users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                yield user

if __name__ == "__main__":
    try:
        # When run as a script, consume the generator
        for user in batch_processing(50):
            print(user)
    except BrokenPipeError:
        sys.stderr.close()
