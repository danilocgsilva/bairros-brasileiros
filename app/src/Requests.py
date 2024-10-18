from flask import Flask, request

class Requests:
    def __init__(self):
        self.dados_json = request.json
    
    def buscar_dados(self, nome_request: str):
        if nome_request == 'buscar_nome_estado_e_cidade':
            return self._buscar_nome_estado_e_cidade()
        if nome_request == 'buscar_nome_cidade_e_bairro':
            return self._buscar_nome_cidade_e_bairro()
        if nome_request == 'buscar_dados_request_nova_receita':
            return self._buscar_dados_request_nova_receita()
        if nome_request == 'receita_id':
            return self._buscar_id_receita()
        raise Exception('Nome da request {} não existe.'.format(nome_request))
            
    def _buscar_nome_estado_e_cidade(self):
        return self.dados_json["nome"], self.dados_json["estado"]
    
    def _buscar_nome_cidade_e_bairro(self):
        return self.dados_json["cidade"], self.dados_json["nome"]
    
    def _buscar_dados_request_nova_receita(self):
        nome = self.dados_json["nome"]
        seletor_tabela = self.dados_json["seletor_tabela"]
        seletor_coluna = self.dados_json["seletor_coluna"]
        endereco = self.dados_json["endereco"]
        
        return nome, seletor_tabela, seletor_coluna, endereco
    
    def _buscar_id_receita(self):
        return self.dados_json["receita_id"]