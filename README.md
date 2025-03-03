# Lima Air Quality

## Overview

The **Lima Air Quality** project is designed to collect, process, store, and analyze air quality data in Lima, Peru. By leveraging AWS cloud services, the system ensures scalability, reliability, and real-time monitoring. 

This project consists of three main components:
1. **Database**: Stores structured air quality data collected from various sensors.
2. **Data Pipeline**: Automates the collection, formatting, and storage of air quality data.
3. **Dashboard**: Provides visual insights into air quality trends and historical data.

---

## Content

- [Architecture](#architecture)
  - [Database](#database)
  - [Data Pipeline](#data-pipeline)
  - [Dashboard](#dashboard)
- [Usage](#usage)

---

## Architecture

### Database

The database is hosted on **AWS RDS (MySQL)** and is responsible for storing all air quality data. It consists of tables that keep track of sensor locations and recorded measurements.

<p align="center">
    <img src="https://github.com/user-attachments/assets/60f19eb5-52f6-48df-bb7c-4b623837d43b" alt="Database Architecture">
</p>

**Key Tables:**
- **Places**: Stores information about sensor locations.
- **Air**: Stores air quality measurements such as CO, NO₂, O₃, PM2.5, and temperature.

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

### Dashboard

The dashboard provides **interactive visualizations and analytical insights** into the air quality trends in Lima. It connects to the database and displays metrics such as **historical trends, real-time air quality index, and pollutant levels**.

<p align="center">
    <img src="https://github.com/user-attachments/assets/3d2f1b2e-8f4e-4b8e-9b6e-3b2f1b2e8f4e" alt="Dashboard Screenshot">
</p>

You can access the live dashboard [here](https://your-dashboard-link.com).

---

## Usage

### Clone the Repository
```bash
git clone https://github.com/your-repo/lima-air-quality.git
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

