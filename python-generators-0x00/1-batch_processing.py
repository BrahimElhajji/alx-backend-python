#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """Yields rows in batches from the database."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",  # replace with your password
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch  # Yield the whole batch

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes each batch and yields users over age 25."""
    for batch in stream_users_in_batches(batch_size):  # 1 loop
        for user in batch:  # 2nd loop
            if user['age'] > 25:
                yield user  # ✅ Use yield, NOT print
