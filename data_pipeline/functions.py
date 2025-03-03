import requests
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


def access_data(place):
    url_base = "https://api.waqi.info/feed/"
    url_end = f"/?token={os.getenv("TOKEN")}"
    
    url = url_base + place + url_end
    
    try:
        driver = requests.get(url)
        driver.raise_for_status() 
        data_json = driver.json()
        if data_json['status'] != 'error': 
            return data_json['data']
    
    except requests.exceptions.RequestException as e:
        print(f"Error accessing data: {e}")
        return None
    
    except e:
        print(f"Error accessing data: {e}")
        return None

def formatting_data(sensor_id, data):
    datetime = data['time']['s']
    
    variables = ['co', 'h', 'no2', 'o3', 'p', 'pm10', 'pm25', 'so2', 't']
    values = (sensor_id, datetime,)
    
    for variable in variables:
        try:
            result = data['iaqi'][variable]['v']
        except KeyError:
            result = None
        values = values + (result,)
    return values