#!/usr/bin/python3
import csv
import mysql.connector
import uuid

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_mysql_password"  # replace with your actual MySQL root password
DB_NAME = "ALX_prodev"

def connect_db():
    """Connect to MySQL server (without specifying database)."""
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to DB server: {err}")
        return None

def create_database(connection):
    """Create ALX_prodev database if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

def connect_to_prodev():
    """Connect to ALX_prodev database."""
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

def create_table(connection):
    """Create user_data table."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            )
        """)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def insert_data(connection, csv_file):
    """Insert data from CSV file if it doesn't already exist."""
    try:
        cursor = connection.cursor()
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute("""
                    SELECT COUNT(*) FROM user_data WHERE user_id = %s
                """, (row['user_id'],))
                exists = cursor.fetchone()[0]
                if not exists:
                    cursor.execute("""
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """, (
                        row['user_id'],
                        row['name'],
                        row['email'],
                        row['age']
                    ))
        connection.commit()
        cursor.close()
        print("Data inserted successfully")
    except Exception as err:
        print(f"Error inserting data: {err}")
