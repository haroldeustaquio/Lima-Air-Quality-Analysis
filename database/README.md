# Database 

## Overview

The database for the Lima Air Quality Analysis project is designed to store and manage data related to air quality measurements collected from various locations in Lima, Peru. The database architecture is designed to be scalable and is hosted on AWS, ensuring reliability and performance. The architecture diagram below provides a visual representation of the database setup.

---

**Content**

- [Architecture](#architecture)
- [Tables](#tables)
    - [Places](#places-table)
    - [Air](#air)
    - [Metric Description](#metric-description)

---

## Architecture

<p align="center">
    <img src=https://github.com/user-attachments/assets/e6408af8-7cd7-4581-bcbe-9987d4058335 alt="Architecture Diagram">
</p>

<p align="center"><em>Figure 1: Database architecture in AWS</em></p>

---

## Tables

### Places

This table stores information about the locations where air quality sensors are placed. Each entry represents a unique place with details such as country, city, and sensor ID.

| Column   | Type         | Constraints                |
|----------|--------------|----------------------------|
| id       | INT          | PRIMARY KEY, AUTO_INCREMENT|
| country  | VARCHAR(255) | DEFAULT 'Peru'             |
| city     | VARCHAR(255) | DEFAULT 'Lima'             |
| sensorID | VARCHAR(255) | NOT NULL                   |
| district | VARCHAR(255) |                            |
| url      | VARCHAR(255) |                            |
| geo_x    | FLOAT        |                            |
| geo_y    | FLOAT        |                            |
| source   | VARCHAR(255) |                            |

### Air

This table records the air quality measurements collected by the sensors. Each entry corresponds to a specific reading taken by a sensor at a given time.

| Column      | Type         | Constraints                |
|-------------|--------------|----------------------------|
| id          | INT          | PRIMARY KEY, AUTO_INCREMENT|
| sensorID    | INT          | 🔑 REFERENCES places(id)   |
| date        | DATETIME     |                            |
| co          | FLOAT        |                            |
| humidity    | FLOAT        |                            |
| no2         | FLOAT        |                            |
| o3          | FLOAT        |                            |
| pressure    | FLOAT        |                            |
| pm10        | FLOAT        |                            |
| pm25        | FLOAT        |                            |
| so2         | FLOAT        |                            |
| temperature | FLOAT        |                            |

### Metric Description

This table provides descriptions for the various metrics recorded in the air quality measurements. Each entry corresponds to a specific metric and its description.

| Column      | Type         | Constraints                |
|-------------|--------------|----------------------------|
| metric      | VARCHAR(255) | PRIMARY KEY                |
| description | TEXT         |                            |
