from flask import make_response, request
import re

def minha_resposta(conteudo: str, codigo_erro = 200, mimetype = None):
    if mimetype == None:
        nome_cliente = request.user_agent.string
        if re.search('Gecko', nome_cliente):
            if type(conteudo).__name__ != 'str':
                conteudo = str(conteudo)
            conteudo = re.sub(r"\n", "<br />", conteudo)
            resposta = make_response(conteudo, codigo_erro)
            resposta.mimetype = "text/html"
        else:
            resposta = make_response(conteudo, codigo_erro)
            resposta.mimetype = "text/plain"
        return resposta
    else:
        resposta = make_response(conteudo, codigo_erro)
        resposta.mimetype = mimetype
        return resposta
