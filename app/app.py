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
        # MigracaoDB().migrar_estrutura()
        migrador.migrar_estrutura()
        mensagens += "Banco de dados migrado."
    except mysql.connector.errors.DatabaseError as e:
        if e.errno == 1007:
            mensagens += "A estrutura do banco de dados já tinha sido migrado. Nada foi feito."
        else:
            raise e
        
    try:
        # mensagens_migracao = MigracaoDB().escrever_tipos_localidades()
        mensagens_migracao = migrador.escrever_tipos_localidades()
        mensagens += "\n" + mensagens_migracao
    except Exception as e:
        raise e
        
    return minha_resposta(mensagens)
        
@app.route("/banco/ajuda")
def banco_ajuda():
    ajuda = Ajuda()
        
    return minha_resposta(ajuda.db())
