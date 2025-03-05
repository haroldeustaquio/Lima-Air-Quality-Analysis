CREATE DATABASE IF NOT EXISTS air_data;
USE air_data;

CREATE TABLE IF NOT EXISTS places (
    id INT PRIMARY KEY AUTO_INCREMENT,
    country VARCHAR(255) DEFAULT 'Peru',
    city VARCHAR(255) DEFAULT 'Lima',
    sensorID VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS air (
    id INT PRIMARY KEY AUTO_INCREMENT,
    sensorID INT,
    date DATETIME,
    co FLOAT,
    humidity FLOAT,
    no2 FLOAT,
    o3 FLOAT,
    pressure FLOAT,
    pm10 FLOAT,
    pm25 FLOAT,
    so2 FLOAT,
    temperature FLOAT
    FOREIGN KEY (sensorID) REFERENCES places(id),
);



CREATE TABLE IF NOT EXISTS metrics_description (
    metric VARCHAR(255) PRIMARY KEY,
    description TEXT
);

INSERT INTO metrics_description (metric, description) VALUES
    ('co', 'Carbon Monoxide'),
    ('humidity', 'Humidity'),
    ('no2', 'Nitrogen Dioxide'),
    ('o3', 'Ozone'),
    ('pressure', 'Atmospheric Pressure'),
    ('pm10', 'Particulate Matter <10 µm'),
    ('pm25', 'Particulate Matter <2.5 µm'),
    ('so2', 'Sulfur Dioxide'),
    ('temperature', 'Temperature');



INSERT INTO places (sensorID) VALUES
    ('peru/lima/san-martin-de-porres'),
    ('peru/lima/carabayllo'),
    ('peru/lima/us-embassy'),
    ('peru/lima/santa-anita'),
    ('peru/lima/puente-piedra'),
    ('peru/lima/campo-de-marte'),
    ('peru/lima/san-borja'),
    ('peru/lima/san-juan-de-lurigancho'),
    ('peru/lima/villa-maria-del-triunfo'),
    ('A486733');

SELECT * FROM places;


ALTER TABLE air_data.places
ADD COLUMN name VARCHAR(255),
ADD COLUMN url VARCHAR(255),
ADD COLUMN geo_x FLOAT,
ADD COLUMN geo_y FLOAT,
ADD COLUMN source VARCHAR(255);

UPDATE air_data.places
SET name = 'San Martin De Porres', url = 'https://aqicn.org/city/peru/lima/san-martin-de-porres', geo_x = -12.00889, geo_y = -77.08447, source = 'SENAMHI'
WHERE sensorID = 'peru/lima/san-martin-de-porres';

UPDATE air_data.places
SET name = 'Campo De Marte', url = 'https://aqicn.org/city/peru/lima/campo-de-marte', geo_x = -12.07054, geo_y = -77.04322, source = 'SENAMHI'
WHERE sensorID = 'peru/lima/campo-de-marte';

UPDATE air_data.places
SET name = 'San Borja', url = 'https://aqicn.org/city/peru/lima/san-borja', geo_x = -12.10859, geo_y = -77.00769, source = 'SENAMHI'
WHERE sensorID = 'peru/lima/san-borja';

UPDATE air_data.places
SET name = 'San Juan De Lurigancho', url = 'https://aqicn.org/city/peru/lima/san-juan-de-lurigancho', geo_x = -11.98164, geo_y = -76.99925, source = 'SENAMHI'
WHERE sensorID = 'peru/lima/san-juan-de-lurigancho';

UPDATE air_data.places
SET name = 'Villa Maria Del Triunfo', url = 'https://aqicn.org/city/peru/lima/villa-maria-del-triunfo', geo_x = -12.16639, geo_y = -76.92, source = 'SENAMHI'
WHERE sensorID = 'peru/lima/villa-maria-del-triunfo';

UPDATE air_data.places
SET name = 'Carabayllo', url = 'https://aqicn.org/city/peru/lima/carabayllo', geo_x = -11.90219, geo_y = -77.03364, source = 'SENAMHI'
WHERE sensorID = 'peru/lima/carabayllo';

UPDATE air_data.places
SET name = 'US Embassy', url = 'https://aqicn.org/city/peru/lima/us-embassy', geo_x = -12.1052081, geo_y = -76.9709299, source = 'US Embassy'
WHERE sensorID = 'peru/lima/us-embassy';

UPDATE air_data.places
SET name = 'Santa Anita', url = 'https://aqicn.org/city/peru/lima/santa-anita', geo_x = -12.04302, geo_y = -76.97144, source = 'SENAMHI'
WHERE sensorID = 'peru/lima/santa-anita';

UPDATE air_data.places
SET name = 'Puente Piedra', url = 'https://aqicn.org/city/peru/lima/puente-piedra', geo_x = -11.86325, geo_y = -77.07413, source = 'SENAMHI'
WHERE sensorID = 'peru/lima/puente-piedra';

UPDATE air_data.places
SET name = 'Santa Clara', url = 'https://aqicn.org/station/@486733', geo_x = -12.01718, geo_y = -76.880539, source = 'Ciencia ciudadana por la Calidad del Aire'
WHERE sensorID = 'A486733';