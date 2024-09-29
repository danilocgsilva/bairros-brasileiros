from flask import Flask, request
from MigracaoDB import MigracaoDB
from src.Ajuda import Ajuda
from src.minha_resposta import minha_resposta
import mysql.connector
from logging.config import dictConfig
import re

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }
)

app = Flask(__name__)

@app.route("/")
def default():
    return "Bairros brasileiros"

@app.route("/banco/migrar")
def migrar():
    try:
        MigracaoDB().migrar()
        return minha_resposta("Banco de dados migrado.")
    except mysql.connector.errors.DatabaseError as e:
        if e.errno == 1007:
            return minha_resposta("O banco de dados já tinha sido migrado. Nada foi feito.")
        else:
            raise e
        
@app.route("/banco/ajuda")
def banco_ajuda():
    ajuda = Ajuda()
        
    return minha_resposta(ajuda.db())
