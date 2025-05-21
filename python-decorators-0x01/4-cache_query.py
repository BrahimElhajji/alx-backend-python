import time
import sqlite3
import functools

# cache global To store query results
query_cache = {}

# Decorator task 1: connection handler
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator: cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get("query")
        if not query and len(args) > 1:
            query = args[1]  # args[0] = conn, args[1] = query

        if query in query_cache:
            print("[CACHE] Returning cached result for query.")
            return query_cache[query]

        print("[DB] Executing and caching result.")
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call → will hit DB and cache
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call → will return cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
