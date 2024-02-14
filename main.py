pip install psycopg2
import os
import json
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Define database connection parameters
db_params = {
    'database': "lab1.2",
    'user': "postgres",
    'password': "IMissPinole1312!?",
    'host': "34.16.107.82",
    'port': "5432"
}

# Connect to your PostGIS database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

@app.route("/")
def hello_world():
    return "Yep!"

@app.route("/hello")
def hello():
    return "hello"

@app.route("/polygon")
def get_polygon_geojson():
    # Fetch the polygon from the database
    cur.execute("SELECT ST_AsGeoJSON(geom) FROM your_polygon_table LIMIT 1;")
    row = cur.fetchone()
    geojson_polygon = row[0]

    # Convert the polygon to a Python dictionary
    polygon_dict = json.loads(geojson_polygon)

    return jsonify(polygon_dict)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
