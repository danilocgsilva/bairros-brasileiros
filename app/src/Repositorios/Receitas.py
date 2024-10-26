from entidades.Receita import Receita
from src.Repositorios.Conexao import Conexao
from crawler.parseadores.XNext import XNext
from crawler.processadores.ProcessadorCapturaCidadeSigla import ProcessadorCapturaCidadeSigla

class Receitas(Conexao):
    def salva(
        self, 
        nome_receita: str, 
        seletor_tabela: str, 
        parseador_string: str,
        processador_string: str, 
        endereco: str,
        tipo_localidade: str
    ):
        query = "INSERT INTO receitas (" + self._buscarStringCamposSemId() + ") VALUES (%s, %s, %s, %s, %s, %s);"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (nome_receita, seletor_tabela, parseador_string, processador_string, endereco, tipo_localidade))
        self.recursodb.commit()
    
    def buscar_por_id(self, id: int) -> Receita:
        query = "SELECT id, " + self._buscarStringCamposSemId() + " FROM receitas WHERE id = %s;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query, (id, ))
        meus_resultados = local_cursor.fetchall()
        receitas_encontradas = []
        for dado_cru in meus_resultados:
            
            parseador = None
            parseador_string = dado_cru[3]
            if parseador_string == "XNext(2, 1)":
                parseador = XNext(2, 1)
            else:
                raise Exception("Não conheço esse parseador")
            
            receita = Receita(
                dado_cru[0], 
                dado_cru[1], 
                dado_cru[2], 
                self._buscarParseadorPelaString(dado_cru[3]), 
                self._buscarProcessadorPelaString(dado_cru[4]), 
                dado_cru[5], 
                dado_cru[6]
            )
            receitas_encontradas.append(receita)
        if len(receitas_encontradas) == 0:
            raise Exception("Não foi encontrada a receita no banco de daddos de id = {}.".format(id))
        return receitas_encontradas[0]
    
    def todas(self) -> list:
        query = "SELECT id, " + self._buscarStringCamposSemId() + " FROM receitas;"
        local_cursor = self.recursodb.cursor()
        local_cursor.execute(query)
        meus_resultados = local_cursor.fetchall()
        receitas_encontradas = []
        for dado_cru in meus_resultados:
            receita = Receita(dado_cru[0], dado_cru[1], dado_cru[2], self._buscarParseadorPelaString(dado_cru[3]), dado_cru[4], dado_cru[5], dado_cru[6])
            receitas_encontradas.append(receita)
        return receitas_encontradas
    
    def _buscarStringCamposSemId(self) -> str:
        return "nome, seletor_tabela, parseador, processador, endereco, tipo_localidade"
    
    def _buscarParseadorPelaString(self, parseador_string: str):
        if parseador_string == "XNext(2, 1)":
            return XNext(2, 1)
        raise Exception("Não conheço esse parseador")
    
    def _buscarProcessadorPelaString(self, processador_string: str):
        if processador_string == "ProcessadorCapturaCidadeSigla":
            return ProcessadorCapturaCidadeSigla()
        raise Exception("Não conheço esse processador")
    