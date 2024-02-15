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
    geojson_with_slashes = cur.fetchone()[0]
    conn.close()
    # Remove the slashes from the GeoJSON string
    geojson_without_slashes = json.loads(geojson_with_slashes.replace("\\", ""))
    return geojson_without_slashes

@app.route('/')
def get_geojson():
    table_name = "labtable"
    geom_column = "geom"
    geojson = fetch_geom_as_geojson(table_name, geom_column, db_params)
    feature_collection = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": geojson,
                "properties": {}
            }
        ]
    }
    return jsonify(feature_collection)

if __name__ == '__main__':
    app.run(debug=True)
