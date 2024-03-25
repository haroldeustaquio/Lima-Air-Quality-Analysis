from funciones import *
import pandas as pd
from time import sleep


while True:
    conn = conect_db()

    air_data = pd.read_sql_query("SELECT * FROM air_data", conn)

    clean_data(air_data).to_csv('data/air_data.csv',index=False)

    # place = pd.read_sql_query("select * from place_data",conn)
    # place['location']= place['location'].apply(lambda x: clean_string(x))
    # place['distrito']= place['distrito'].apply(lambda x: clean_string(x))
    # place.to_csv("data/place.csv",index=False)

    print("Hecho")
    sleep
    sleep(1807)