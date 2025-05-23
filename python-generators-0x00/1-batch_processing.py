#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that fetches users in batches from the database."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",  # Replace with your actual MySQL password
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            return
        yield batch

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes batches and filters users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):               # loop 1
        for user in batch:                                          # loop 2
            if user['age'] > 25:
                print(user)                                         # counts as logic, not a loop
