from flask import Flask, jsonify
import psycopg2
import json

# Initialize Flask app
app = Flask(__name__)

# Database connection parameters
db_params = {
    'database': "lab1.2",
    'user': "postgres",
    'password': "IMissPinole1312!?",
    'host': "34.16.107.82",
    'port': "5432"
}

def fetch_geom_as_geojson(table_name, geom_column, db_params):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    cur.execute(f"SELECT ST_AsGeoJSON({geom_column}) FROM {table_name} LIMIT 1")
    geojson_string = cur.fetchone()[0]
    conn.close()
    # Decode JSON string twice to get the GeoJSON object
    geojson_object = json.loads(json.loads(geojson_string))
    # Modify the GeoJSON object to follow the specified format
    feature = {
        "type": "Feature",
        "geometry": geojson_object,
        "properties": {}
    }
    return feature

@app.route('/')
def get_geojson():
    table_name = "labtable"
    geom_column = "geom"
    geojson = fetch_geom_as_geojson(table_name, geom_column, db_params)
    return jsonify(geojson)

if __name__ == '__main__':
    app.run(debug=True)
