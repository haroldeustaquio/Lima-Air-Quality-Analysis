from funciones import *

places = ["peru/lima/san-martin-de-porres","peru/lima/campo-de-marte","peru/lima/san-borja","peru/lima/san-juan-de-lurigancho",
        "peru/lima/villa-maria-del-triunfo","@7581","A408442","A473740",
        "A475105","A470218","A408151","A408133","A248224",
        "A474319","A474313","A468256","A471052","A466591","A472096",
        "A408361",
        "A408370",
        "A408367"]


conn = conect_db()
cursor = conn.cursor()
for i,place in enumerate(places,start=1):
    content = access_data(place)
    values = (get_values_place(content),)
    table = "place_data"
    cols = "distrito"
    query = f"UPDATE {table} SET {cols} = ? WHERE id_place = {i}"
    cursor.execute(query, values)
    print("hecho")
    
conn.commit()
conn.close()