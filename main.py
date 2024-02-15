from flask import Flask, jsonify
import psycopg2

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
    geojson = cur.fetchone()[0]
    conn.close()
    return geojson

@app.route('/')
def get_geojson():
    table_name = "labtable"
    geom_column = "geom"
    geojson = fetch_geom_as_geojson(table_name, geom_column, db_params)
    return jsonify(geojson)

if __name__ == '__main__':
    app.run(debug=True)


# Run the Flask app, when the file is run 
if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=8080)
