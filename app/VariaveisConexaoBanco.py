import os

class VariaveisConexaoBanco:
    def buscarHost(self):
        return os.environ.get('BAIRROS_BRASILEIROS_DB_HOST')
    
    def buscarNomeDoBanco(self):
        return os.environ.get('BAIRROS_BRASILEIROS_DB_NOME')
    
    def buscarUsuarioBanco(self):
        return os.environ.get('BAIRROS_BRASILEIROS_DB_USUARIO')
    
    def buscarSenhaBanco(self):
        return os.environ.get('BAIRROS_BRASILEIROS_DB_SENHA')
