# Project Name
Tumor Classification

## Overview

This project is used to classify whether there is tumor inside the kidney or not. If there is tumor it gives output as "Tumor" otherwise it gives "Normal"

### Requirements

- Python 
- MySQL 

### Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Database Setup

-  Install MySQL Server
-  Create a Database and Tables

```bash
CREATE DATABASE IF NOT EXISTS your_database_name;
USE your_database_name;

-- Create tables
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
- Define other columns and constraints
);
```
-Configure Database in database/db_operation.py 
```bash
DB_HOST = 'localhost' --> Provide the localhost.
DB_USER = 'your_username' ---> Give the username inplace of 'your_username'
DB_PASSWORD = 'your_password'  ---> Give password
DB_NAME = 'your_database_name' ---> Enter the database name
```
### Usage
Run the application
```bash
python app.py
```

### Access the application

-  Open a web browser and navigate to http://localhost:8080

###  Predict ouput

-  For the prediction use the "Test Images Data" inside the project folder at artifacts/data_ingestion .




