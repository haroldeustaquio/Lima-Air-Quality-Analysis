# Database 

## Overview

The database for the Lima Air Quality Analysis project is designed to store and manage data related to air quality measurements collected from various locations in Lima, Peru.

The database architecture is designed to be scalable and is hosted on AWS, ensuring reliability and performance. The architecture diagram below provides a visual representation of the database setup.

---

**Content**

- [Architecture](#architecture)
- [Tables](#tables)
    - [Places](#places-table)
    - [Air](#air)

---

## Architecture

<p align="center">
    <img src="https://github.com/user-attachments/assets/c23566b3-5f31-4520-a88b-feb54ca1b155" alt="Architecture Diagram">
</p>

<p align="center"><em>Figure 1: Database architecture in AWS</em></p>

---

## Tables

### Places

This table stores information about the locations where air quality sensors are placed. Each entry represents a unique place with details such as country, city, and sensor ID.

| Column    | Type         | Constraints                |
|-----------|--------------|----------------------------|
| id        | INT          | PRIMARY KEY, AUTO_INCREMENT|
| country   | VARCHAR(255) | DEFAULT 'Peru'             |
| city      | VARCHAR(255) | DEFAULT 'Lima'             |
| sensorID  | VARCHAR(255) | NOT NULL                   |

### Air

This table records the air quality measurements collected by the sensors. Each entry corresponds to a specific reading taken by a sensor at a given time.

| Column      | Type         | Constraints                |
|-------------|--------------|----------------------------|
| id          | INT          | PRIMARY KEY, AUTO_INCREMENT|
| sensorID    | INT          | 🔑 REFERENCES places(id)    |
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


