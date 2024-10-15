from src.DadoLegivel import DadoLegivel

class Locais:
    def listar_todos_dados(self) -> list:
        query = "SELECT lo.local, tl.tipo FROM locais lo LEFT JOIN tipos_locais tl ON tl.id = lo.tipo_localidade;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query)
        meus_resultados = local_cursor.fetchall()
        dados_legiveis = []
        for dado_cru in meus_resultados:
            dados_legiveis.append(DadoLegivel(dado_cru[0], dado_cru[1]))
        return dados_legiveis