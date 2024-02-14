import os
import json
from flask import Flask, jsonify
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry

app = Flask(__name__)

# Define database connection parameters
db_params = {
    'database': "lab1.2",
    'user': "postgres",
    'password': "IMissPinole1312!?",
    'host': "34.16.107.82",
    'port': "5432"
}

# Create a SQLAlchemy engine
engine = create_engine(f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define your SQLAlchemy metadata
metadata = MetaData()

# Define your polygon table
polygon_table = Table('labtable', metadata, autoload=True, autoload_with=engine, extend_existing=True)

@app.route("/polygon")
def get_polygon_geojson():
    # Query the polygon from the database
    result = session.query(polygon_table).limit(1).first()
    
    # Convert the geometry column to GeoJSON
    geojson_polygon = session.scalar(result.geom.ST_AsGeoJSON())

    # Convert the GeoJSON string to a Python dictionary
    polygon_dict = json.loads(geojson_polygon)

    return jsonify(polygon_dict)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
