# Data Pipeline

## Overview

The data pipeline for the Lima Air Quality project is designed to collect, process, and store air quality data from various sensors. The pipeline leverages AWS services for data storage, ensuring scalability and reliability. The main components of the pipeline include:

1. **Data Ingestion**: Data is retrieved from the World Air Quality Index (WAQI) API, which provides real-time air quality information for different locations.
2. **Data Formatting**: The raw data is filtered and formatted to ensure consistency and compatibility with the database schema.
3. **Data Storage**: The transformed data is stored in a MysSQL database hosted on AWS RDS, allowing for efficient querying and analysis.

This pipeline enables continuous monitoring and analysis of air quality in Lima, providing valuable insights for researchers and policymakers.

**Content**

- [Architecture](#architecture)
- [Functions](#functions)

---


## Architecture


<p align="center">
    <img src=https://github.com/user-attachments/assets/acb4aead-e449-4caf-a516-a0b3c774f111 alt="Architecture Diagram">
</p>

<p align="center"><em>Figure 1: Data Pipeline in AWS</em></p>


---
## Functions

The `functions.py` module contains the necessary functions for connecting to the database, obtaining data from the air quality API, and transforming this data before storing it.

### Database Connection
- **`connect_db()`**: Establishes a connection to the PostgreSQL database hosted on AWS RDS using credentials stored in environment variables.
- **`execute_bulk_insert(table, columns, values)`**: Inserts multiple records into a specific table in a single execution to improve efficiency.
- **`select_query(query)`**: Executes an SQL query and returns the results.

### Data Retrieval
- **`access_data(place)`**: Connects to the air quality API (WAQI) and retrieves real-time data for a specific location.
  
### Data Transformation
- **`formatting_data(sensor_id, data)`**: Extracts and structures the air quality data into a suitable format for storage in the database.
