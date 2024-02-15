import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_geojson_from_postgis():
    # Connect to the database
    conn = psycopg2.connect(
        database="lab1.2",
        user="postgres",
        password="IMissPinole1312!?",
        host="34.16.107.82",
        port="5432"
    )

    # Retrieve data
    with conn.cursor() as cur:
        # Query to get GeoJSON
        cur.execute("SELECT ST_AsGeoJSON(geom)::json FROM labtable;")
        # Fetch
        data = cur.fetchall()

    # Close the connection
    conn.close()

    # Extract GeoJSON data from the result
    geojson_data = [row[0] for row in data]

    return geojson_data

@app.route('/data')
def data():
    # Get GeoJSON from PostGIS
    geojson_data = get_geojson_from_postgis()
    return jsonify(geojson_data)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
