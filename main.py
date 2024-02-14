from flask import Flask
# Initialize the app 
app = Flask(__name__) 
# This is our index route --- when we go to the main URL, this is what gets returned 
# In this case, we also specify that this is a 'GET' HTTP request method 
@app.route("/", methods=["GET"]) 
def index(): 
    return "You made it! The API is working." 
# Run the Flask app, when the file is run 
if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=8080) 
