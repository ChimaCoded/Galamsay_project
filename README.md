# Galamsay Analysis API Project

This project analyzes dataset on illegal small-scale mining activities (Galamsay) in Ghana and exposes the results via a RESTful API. The API calculates the following: 

- Total number of Galamsay sites across all cities. 
- Region with the highest number of Galamsay sites.
- List cities where the Galamsay sites exceed a given threshold (e.g. 10).
- Average number of Galamsay sites per region.

## Features
Data Analysis:
Calculate the total number of Galamsay sites across all cities.
Identify the region with the highest number of Galamsay sites.
List cities where the number of Galamsay sites exceeds a given threshold (10, 20, 35).
Calculate the average number of Galamsay sites per region.

RESTful API:
Exposes analysis results via HTTP endpoints.

Database Logging:
Logs analysis results to an SQLite database for future reference.

## Setup
## Prerequisites
Python 3.8 or higher

## Installation
### Clone the Repository:
git clone <repository-url>
cd galamsay_project

### Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate.bat

### Install requirements.txt
pip install -r requirements.txt

### Load the Dataset: 
Ensure galamsay_data.xlsx file is in the data/ folder.


## Running the API
Start the Server:
python app.py

Access the API:
The API is accessed via http://127.0.0.1:5000
Use API testing tools like Postman

Running Tests:
python -m unittest tests/test_galamsayAPI.py


## API Endpoints
GET /analysis

Response: 
![image](https://github.com/user-attachments/assets/30c924b5-5fcc-43b1-b2f4-236594a10163)







