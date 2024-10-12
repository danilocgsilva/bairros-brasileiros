from src.TiposLocais import TiposLocais

class DadoLegivel:
    def __init__(self, nome: str, tipo: str):
        if not tipo in [TiposLocais.bairro.name, TiposLocais.cidade.name, TiposLocais.estado.name]:
            mensagem_excessao = 'O tipo ' + tipo + ' não é válido.'
            raise Exception(mensagem_excessao)
        self.nome = nome
        self.tipo = tipo