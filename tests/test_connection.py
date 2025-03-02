import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=int(os.getenv("DB_PORT"))
        )
        print("Connection Successfully")
        return conn
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

connect_db()