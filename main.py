# Import packages 
from flask import Flask 
import psycopg2 


# Initialize the app 
app = Flask(__name__) 
# Create index route 
@app.route("/", methods=["GET"]) 
def index(): 
    return "You made it! The API is working." 
# Create data route 
@app.route("/data", methods=["GET"]) 
def data(): 
    # Connect to the database 
    conn = psycopg2.connect( 
        host="34.16.107.82", 
        database="lab1.2", 
        user="postgres", 
        password="IMissPinole1312!?", 
        port=5432, 
    )

    # Retrieve data 
    with conn.cursor() as cur: 
        # Query to get data 
        cur.execute("SELECT ST_AsGeoJSON(\"lab table\".*)::json FROM \"lab table\";")
        # Fetch 
        data = cur.fetchall() 
    # Do some processing here (if needed) 
    # ... 
    # Close the connection 
    conn.close() 
    # Return the data 
    return data 


# Run the Flask app, when the file is run 
if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=8080) 
