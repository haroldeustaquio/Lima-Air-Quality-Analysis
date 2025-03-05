# Air Quality Lima

## Overview

The **Lima Air Quality** project is designed to collect, process, store, and analyze air quality data in Lima, Peru. By leveraging AWS cloud services, the system ensures scalability, reliability, and real-time monitoring. 

This project consists of three main components:
1. **Database**: Stores structured air quality data collected from various sensors.
2. **Data Pipeline**: Automates the collection, formatting, and storage of air quality data.
3. **Dashboard**: Provides visual insights into air quality trends and historical data.

---

## Content

- [Dashboard](#dashboard)
- [Architecture](#architecture)
  - [Database](#database)
  - [Data Pipeline](#data-pipeline)
- [Usage](#usage)

---

## Dashboard

The dashboard provides **interactive visualizations** into the air quality trends in Lima. It connects to the database and displays metrics such as **historical trends, real-time sensor information**.

You can access the live dashboard [here](https://acortar.link/xXBReb).

<p align="center">
    <img src="https://github.com/user-attachments/assets/09a76a18-0758-4607-b940-09ed7af3d605" alt="Dashboard Screenshot">
</p>


---

## Architecture

### Database

The database is hosted on **AWS RDS (MySQL)** and is responsible for storing all air quality data. It consists of tables that keep track of sensor locations and recorded measurements.

<p align="center">
    <img src="https://github.com/user-attachments/assets/e6408af8-7cd7-4581-bcbe-9987d4058335" alt="Database Architecture">
</p>

**Key Tables:**

- **Places**: Stores information about the locations where air quality sensors are placed. Each entry includes details such as country, city, sensor ID, district, URL, geographical coordinates, and data source.
- **Air**: Records air quality measurements collected by the sensors. Each entry includes the sensor ID, date, and various pollutant levels such as CO, NO₂, O₃, PM10, PM2.5, SO₂, humidity, pressure, and temperature.
- **Metric Description**: Provides descriptions for the various metrics recorded in the air quality measurements, detailing what each metric represents.

---

### Data Pipeline

The data pipeline is responsible for **automating data ingestion, formatting, and storage**. It retrieves air quality data from the **World Air Quality Index (WAQI) API**, formats it, and inserts it into the database.

<p align="center">
    <img src="https://github.com/user-attachments/assets/acb4aead-e449-4caf-a516-a0b3c774f111" alt="Data Pipeline Architecture">
</p>

#### Key Functions:
- **Data Retrieval**: Fetches real-time air quality data via API.
- **Data Formatting**: Structures and formatting the data.
- **Data Storage**: Inserts formatted data into the database.

---

## Usage

### Clone the Repository
```bash
git clone https://github.com/haroldeustaquio/Air-Quality-Lima
cd lima-air-quality
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a ``.env`` file in the root directory and add the following credentials:

```bash
DB_HOST=your-db-host
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
API_KEY=your-waqi-api-key
```

