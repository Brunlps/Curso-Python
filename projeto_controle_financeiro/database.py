import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'endfinance_user',
        password = 'endfinance123',
        database = 'endfinance'
    )