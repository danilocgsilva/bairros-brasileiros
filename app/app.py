from flask import Flask, request
from MigracaoDB import MigracaoDB
from src.Ajuda import Ajuda
from src.minha_resposta import minha_resposta
import mysql.connector

app = Flask(__name__)

@app.route("/")
def default():
    return "Bairros brasileiros"

@app.route("/banco/migrar")
def migrar():
    migrador = MigracaoDB()
    mensagens = ""
    
    try:
        migrador.migrar_estrutura()
        mensagens += "Banco de dados migrado."
    except mysql.connector.errors.DatabaseError as e:
        if e.errno == 1007:
            mensagens += "O banco de dados já tinha sido migrado. Nada foi feito."
        else:
            raise e
        
    try:
        migrador.escrever_tipos_localidades()
        mensagens += "\nInserido os tipos de locais."
    except Exception as e:
        raise e
        
    return minha_resposta(mensagens)
        
@app.route("/banco/ajuda")
def banco_ajuda():
    ajuda = Ajuda()
        
    return minha_resposta(ajuda.db())
