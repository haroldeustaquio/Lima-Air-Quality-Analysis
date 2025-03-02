import requests
import json
import pandas as pd 
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

def select_query(query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def execute_bulk_insert(table, columns, values):
    """Ejecuta una inserción masiva en una sola conexión."""
    conn = connect_db()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        placeholders = ", ".join(["%s"] * len(columns))
        column_names = ", ".join(columns)
        query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
        
        cursor.executemany(query, values)
        conn.commit()
        print(f"{cursor.rowcount} rows inserted successfully.")

    except pymysql.Error as e:
        print(f"Error executing bulk insert: {e}")
    finally:
        conn.close()

def access_data(place):
    url_base = "https://api.waqi.info/feed/"
    url_end = "/?token=fcf6d16f5e903de70c76f7c7b5eee3fa8ba79a4b"
    
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












def clean_data(df):
    # Change the type of datetime
    df.datetime = pd.to_datetime(df.datetime)
    # Drop duplicates 
    df.drop_duplicates(inplace=True)
    # Drop null values
    df.dropna(subset=['dominentpol'],inplace=True)
    # Drop column: id
    df.drop(columns=['id',"dominentpol"],inplace=True)

    value = df[df.id_place==3].so2.mean()
    df[df.id_place==3].fillna(value)    
    
    df = df.groupby(['id_place', pd.Grouper(key='datetime', freq='30min')]).mean().round(2).reset_index()
    columns_to_normalize = ['co', 'h', 'no2', 'o3', 'p', 'pm10', 'pm25', 'so2', 't', 'wg']
    df_normalized = df.copy()
    for col in columns_to_normalize:
            temp = df.groupby('id_place')[col].transform(lambda x: (x - x.min()) / (x.max()-x.min()))
            df_normalized[col] = temp

    df_normalized= df_normalized.melt(id_vars=['id_place','datetime'],var_name="contaminant",value_name="value_normalized")
    df = df.melt(id_vars=['id_place','datetime'],var_name="contaminant",value_name="value")
    df_final = pd.merge(df,df_normalized,how="inner",on=['id_place','datetime','contaminant'])
    df_final.contaminant = df_final.contaminant.apply(lambda x: x.upper().replace("25","2.5"))
    
    return df_final