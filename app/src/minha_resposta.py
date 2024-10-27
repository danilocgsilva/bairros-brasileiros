from flask import make_response, request
import re

def minha_resposta(conteudo: str, codigo_erro = 200):
    nome_cliente = request.user_agent.string
    if re.search('Gecko', nome_cliente):
        resposta = make_response(conteudo, codigo_erro)
        conteudo = re.sub(r"\n", "<br />", conteudo)
        resposta.mimetype = "text/html"
    else:
        resposta = make_response(conteudo, codigo_erro)
        resposta.mimetype = "text/plain"
    return resposta
    
