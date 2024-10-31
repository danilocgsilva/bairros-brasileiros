class HistoricoBusca:
    def __init__(
        self,
        id: int, 
        receita_id: int,
        capturadas = None,
        data_inicio = None,
        data_fim = None,
        sucessos = None,
        fracassos = None
    ):
        self.id = id
        self.receita_id = receita_id
        self.capturadas = capturadas
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.sucessos = sucessos
        self.fracassos = fracassos