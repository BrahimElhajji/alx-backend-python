mport time
import sqlite3
import functools

# Decorator task 1: Dealing with database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator: trying again after failure
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    print(f"[INFO] Attempt {attempt}...")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[WARNING] Error on attempt {attempt}: {e}")
                    last_exception = e
                    if attempt < retries:
                        time.sleep(delay) # waiting before trying again
            print("[ERROR] All retry attempts failed.")
            raise last_exception  # Re-upload the last error after all attempts have failed
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Experience bringing users back with retry
users = fetch_users_with_retry()
print(users)
