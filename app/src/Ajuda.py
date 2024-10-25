"""
Classe responsável por informações de ajuda em código.
"""
class Ajuda:
    def db(self):
        """
        Descreve as tabelas do banco de dados.
        """
        texto_ajuda = """O banco de dados é composto de duas tabelas:
locais: que seriam os bairros, mas podendo ser também cidade ou estado.
tipos_locais: tipos de locais. Cidade, bairro, estado, subdistrito, região, etc.
receitas: as receitas são os dados para a busca das informações de localidades
"""
        return texto_ajuda