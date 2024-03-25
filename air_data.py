from time import sleep
from funciones import *

while (True):
    places = ["peru/lima/san-martin-de-porres",
            "peru/lima/campo-de-marte",
            "peru/lima/san-borja",
            "peru/lima/san-juan-de-lurigancho",
            "peru/lima/villa-maria-del-triunfo","@7581", "A408442","A473740","A475105","A470218","A408151","A408133","A248224",
            "A474319","A474313","A468256","A471052","A466591","A472096",
            "A408361",
            "A408370",
            "A408367",]

    conn = conect_db()
    cursor = conn.cursor()
    for i,place in enumerate(places,start=1):
        content = access_data(place)

        values = (i,) + get_values_data(content)
        table = "air_data"
        cols = "id_place, datetime, dominentpol, co, h, no2, o3, p, pm10, pm25, so2, t, wg"
        query = f"INSERT INTO {table} ({cols}) VALUES ({', '.join(['?' for _ in values])})"
        cursor.execute(query, values)
        print(f"hecho x{i}")

    conn.commit()
    conn.close()
    sleep(150)
