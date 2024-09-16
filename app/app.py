from flask import Flask
from MigracaoDB import MigracaoDB
import mysql.connector

app = Flask(__name__)

@app.route("/")
def migrar():
    try:
        MigracaoDB().migrar()
        return "Banco de dados migrado."
    except mysql.connector.errors.DatabaseError as e:
        if e.errno == 1007:
            return "O banco de dados já tinha sido migrado. Nada foi feito."
        else:
            raise e
