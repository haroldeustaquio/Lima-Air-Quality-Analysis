import functions as f


database_creation = "CREATE DATABASE IF NOT EXISTS air_data"
f.execute_query(database_creation)

table_creation_1 = """
create table if not exists air_data.places(
    id int primary key auto_increment,
    country varchar(255) default 'Peru',
    city varchar(255) default 'Lima',
    sensorID varchar(255)
)
"""


table_creation_2 = """
create table if not exists air_data.air(
    id int primary key auto_increment,
    sensorID varchar(255),
    date datetime,
    co float,
    humidity float,
    no2 float,
    o3 float,
    pressure float,
    pm10 float,
    pm25 float,
    so2 float,
    temperature float
)
"""

f.execute_query(table_creation_1)
f.execute_query(table_creation_2)

sensorID = [
    "peru/lima/san-martin-de-porres",
    "peru/lima/campo-de-marte",
    "peru/lima/san-borja",
    "peru/lima/san-juan-de-lurigancho",
    "peru/lima/villa-maria-del-triunfo",
    "peru/lima/carabayllo",
    "peru/lima/us-embassy",
    "peru/lima/santa-anita",
    "peru/lima/puente-piedra",
    "A486733",
]



values = [(sensor,) for sensor in sensorID]
f.execute_bulk_insert("air_data.places", ["sensorID"], values)

print(f.select_query("select * from air_data.places"))