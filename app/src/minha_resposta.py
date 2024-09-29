from flask import make_response, request
import re

def minha_resposta(texto: str):
    nome_cliente = request.user_agent.string
    
    if re.search('Gecko', nome_cliente):
        texto_html = re.sub(r"\n", "<br />", texto)
        resposta = make_response(texto_html)
        resposta.mimetype = "text/html"
        return resposta
        
    resposta = make_response(texto)
    resposta.mimetype = "text/plain"
    return resposta
    
