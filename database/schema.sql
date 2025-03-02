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
    sensorID VARCHAR(255),
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
);



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
