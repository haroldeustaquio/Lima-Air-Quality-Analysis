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
    sensorID int,
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
    FOREIGN KEY (sensorID) REFERENCES air_data.places(id)
)
"""

table_creation_3 = """
CREATE TABLE IF NOT EXISTS air_data.metrics_description (
    metric VARCHAR(255) PRIMARY KEY,
    description TEXT
)
"""


f.execute_query(table_creation_1)
f.execute_query(table_creation_2)
f.execute_query(table_creation_3)

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

metrics_description = [
    ("co", "Carbon Monoxide"),
    ("humidity", "Humidity"),
    ("no2", "Nitrogen Dioxide"),
    ("o3", "Ozone"),
    ("pressure", "Atmospheric Pressure"),
    ("pm10", "Particulate Matter <10 µm"),
    ("pm25", "Particulate Matter <2.5 µm"),
    ("so2", "Sulfur Dioxide"),
    ("temperature", "Temperature")
]


values = [(sensor,) for sensor in sensorID]
f.execute_bulk_insert("air_data.places", ["sensorID"], values)
f.execute_bulk_insert("air_data.metrics_description", ["metric", "description"], metrics_description)


alter_table_query = """
ALTER TABLE air_data.places
ADD COLUMN district varchar(255),
ADD COLUMN url varchar(255),
ADD COLUMN geo_x float,
ADD COLUMN geo_y float,
add column source varchar(255)
"""

f.execute_query(alter_table_query)

sensor_data = [
    ("San Martin De Porres", "https://aqicn.org/city/peru/lima/san-martin-de-porres", -12.00889, -77.08447, "SENAMHI", "peru/lima/san-martin-de-porres"),
    ("Jesús María", "https://aqicn.org/city/peru/lima/campo-de-marte", -12.07054, -77.04322, "SENAMHI", "peru/lima/campo-de-marte"),
    ("San Borja", "https://aqicn.org/city/peru/lima/san-borja", -12.10859, -77.00769, "SENAMHI", "peru/lima/san-borja"),
    ("San Juan De Lurigancho", "https://aqicn.org/city/peru/lima/san-juan-de-lurigancho", -11.98164, -76.99925, "SENAMHI", "peru/lima/san-juan-de-lurigancho"),
    ("Villa Maria Del Triunfo", "https://aqicn.org/city/peru/lima/villa-maria-del-triunfo", -12.16639, -76.92, "SENAMHI", "peru/lima/villa-maria-del-triunfo"),
    ("Carabayllo", "https://aqicn.org/city/peru/lima/carabayllo", -11.90219, -77.03364, "SENAMHI", "peru/lima/carabayllo"),
    ("Santiago De Surco", "https://aqicn.org/city/peru/lima/us-embassy", -12.1052081, -76.9709299, "US Embassy", "peru/lima/us-embassy"),
    ("Santa Anita", "https://aqicn.org/city/peru/lima/santa-anita", -12.04302, -76.97144, "SENAMHI", "peru/lima/santa-anita"),
    ("Puente Piedra", "https://aqicn.org/city/peru/lima/puente-piedra", -11.86325, -77.07413, "SENAMHI", "peru/lima/puente-piedra"),
    ("Ate", "https://aqicn.org/station/@486733", -12.01718, -76.880539, "Ciencia ciudadana por la Calidad del Aire", "A486733"),
]

for data in sensor_data:
    name, url, geo_x, geo_y, source, sensorID = data
    update_query = f"""
    UPDATE air_data.places
    SET district = '{name}', url = '{url}', geo_x = {geo_x}, geo_y = {geo_y}, source = '{source}'
    WHERE sensorID = '{sensorID}'
    """
    f.execute_query(update_query)