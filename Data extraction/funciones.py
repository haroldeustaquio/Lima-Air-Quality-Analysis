import requests
import sqlite3
import json
import pandas as pd 

def access_data(place):
    url_base = "https://api.waqi.info/feed/"
    url_end = "/?token=fcf6d16f5e903de70c76f7c7b5eee3fa8ba79a4b"
    
    url = url_base + place + url_end
    
    try:
        driver = requests.get(url)
        driver.raise_for_status() 
        contenido_json = driver.json()
        return contenido_json
    
    except requests.exceptions.RequestException as e:
        with open('respaldo.json', 'r') as archivo:
            # Carga el contenido del archivo JSON en una variable
            contenido_json = json.load(archivo)        

    return contenido_json

def conect_db():
    conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/Air Quality/air_pollution.db')
    return conn

def insertar_valores(table,cols,values,cursor):
    query = f"INSERT INTO {table} ({cols}) VALUES ({', '.join(['?' for _ in values])})"
    cursor.execute(query, values)

def get_values_place(content):
    
    try:
        location = content['data']['city']['location']
        values = location.split(sep=",")
        if len(values) >= 4:
            return values[3]
        else:
            return ""
    except (KeyError, IndexError):
        return ""

def get_values_data(content):
    datetime = content['data']['time']['s']

    dominentpol = content['data']['dominentpol']

    variables = ['co', 'h', 'no2', 'o3', 'p', 'pm10', 'pm25', 'so2', 't', 'wg']
    values = (datetime,dominentpol,)

    for variable in variables:
        
        try:
            resultado = content['data']['iaqi'][variable]['v']
        except KeyError:
            resultado = None
        values = values + (resultado,)

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



def clean_string(txt:str) -> str:
    txt = (txt).strip()
    tildes = ["á","é","í","ó","ú"]
    reales = ["a","e","i","o","u"]
    for real, tilde in zip(reales, tildes):
        txt = txt.replace(f"{tilde}",f"{real}")  
    return txt.title()