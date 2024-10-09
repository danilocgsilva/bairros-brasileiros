from flask import make_response, request
import re

def minha_resposta(texto: str, codigo_erro = 200):
    nome_cliente = request.user_agent.string
    if re.search('Gecko', nome_cliente):
        resposta = make_response(texto_html, codigo_erro)
        texto_html = re.sub(r"\n", "<br />", texto)
        resposta.mimetype = "text/html"
    else:
        resposta = make_response(texto, codigo_erro)
        resposta.mimetype = "text/plain"
    return resposta
    
