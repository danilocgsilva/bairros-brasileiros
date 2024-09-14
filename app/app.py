from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    path = os.path.join('migrations', 'migration.sql')
    file = open(path, "r")
    query = file.read()
    
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="tiger",
        database="<database_name>"
    )

    
    return query
