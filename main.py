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

@app.route("/", methods=["GET"]) 
def index(): 
    return "{'type': 'MultiPolygon','coordinates': [[[[-74, 40.00012207],[-73, 40.00012207],[-73, 41.00012207],[-74, 41.00012207],[-74, 40.00012207]]]]}"


    
if __name__ == '__main__':
    app.run(debug=True)
