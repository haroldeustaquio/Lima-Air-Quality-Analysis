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

def execute_bulk_insert(table, columns, values):
    """Ejecuta una inserción masiva en una sola conexión."""
    conn = connect_db()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        placeholders = ", ".join(["%s"] * len(columns))  # Genera (%s, %s, %s, ...)
        column_names = ", ".join(columns)  # Convierte ['sensorID'] en 'sensorID'
        query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
        
        cursor.executemany(query, values)  # Inserta todos los valores en una sola ejecución
        conn.commit()
        print(f"{cursor.rowcount} rows inserted successfully.")
    except pymysql.Error as e:
        print(f"Error executing bulk insert: {e}")
    finally:
        conn.close()

def select_query(query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def execute_query(query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()