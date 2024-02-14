import os
import psycopg2
from flask import Flask

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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
