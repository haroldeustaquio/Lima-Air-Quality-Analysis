from dotenv import load_dotenv
import functions as f
load_dotenv()


def lambda_handler(event, context):
    places = f.select_query("SELECT id, sensorID FROM air_data.places")

    total_data = []
    for sensor_id, place in places:
        data = f.access_data(place)
        if data is None:
            continue
        formatted_data = f.formatting_data(sensor_id, data)
        total_data.append(formatted_data)

    columns = ['sensorID', 'date', 'co', 'humidity', 'no2', 'o3', 'pressure', 'pm10', 'pm25', 'so2', 'temperature']
    f.execute_bulk_insert("air_data.air", columns, total_data)

    return {"statusCode": 200, "body": "Data inserted successfully"}