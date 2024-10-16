class Receita:
    def __init__(
        self,
        id: int, 
        nome: str, 
        seletor_tabela: str, 
        seletor_coluna: str,
        endereco: str
    ):
        self.id = id,
        self.nome = nome,
        self.seletor_tabela = seletor_tabela
        self.seletor_coluna = seletor_coluna
        self.endereco = endereco
