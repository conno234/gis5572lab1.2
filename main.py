# Import packages 
from flask import Flask 
import psycopg2 

# Define database connection parameters
db_params = {
    'database': "lab1.2",
    'user': "postgres",
    'password': "IMissPinole1312!?",
    'host': "34.16.107.82",
    'port': "5432"
}

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
    conn = psycopg2.connect(**db_params)
    
    # Retrieve data 
    with conn.cursor() as cur: 
        # Query to get data 
        cur.execute("SELECT ST_AsGeoJSON(labtable.*)::json FROM labtable;") 
        # Fetch 
        data = cur.fetchall() 
    
    # Close the connection 
    conn.close() 
    
    # Return the data 
    return data 

# Run the Flask app, when the file is run 
if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=8080)
