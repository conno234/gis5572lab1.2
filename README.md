## Intro
This repository is in service of completing GIS 5572 Lab 1.2, wherein an ArcGIS Online Notebook is used to create a polygon, convert it into well known text, save it PostGIS, where it is then taken with a Flask App stored on this repo and hosted online as a GeoJSON using Google Cloud Run. 

## Components
* Lab 1.2 ArcGIS Pro Notebook.ipynb: this is the Jupyter notebook that is run in ArcGIS Pro to create the polygons and store it in a PostGIS Database (DATABASE INFO HAS BEEN REMOVED).
* requirements.txt: this file lists the needed modules and packages, as well as their version, for running the other scripts on this repository.
* Dockerfile: this file is used to connect the repository to Google Cloud Run so that it can deploy the app.
* main.py: this contains the flask app code that initiates the app, grabs the WKT info from the PostGIS info, converts it to a GeoJSON, and passes it along to the app.

  ## Usage
  If one wanted to use this repo themselves, they would first need to set up a PostgreSQL database and enable PostGIS in it. From there, one can take the ArcGIS Pro notebook, pout in their own desired vertices and login information for their PostGIS databases. From there, they can copy this repo and use it to create their own Google Cloud Run service (one will have to manually put in their database login info as environment variables in Google Cloud Run). In addition, host and port information in the main.py file may have to be changed based on the configuration on Google Cloud Run. From there, Cloud Run will produce a URL with needed GeoJSON info that can be used for creating layers on ArcGIS Online.
