import unittest
from src.SeparaNomeCidadeSiglaEstado import SeparaNomeCidadeSiglaEstado

class test_SeparaNomeCidadeSiglaEstado(unittest.TestCase):
    def test_sao_paulo(self):
        separador = SeparaNomeCidadeSiglaEstado("São Paulo (SP)")
        cidade, sigla = separador.separa()
        self.assertEqual("São Paulo", cidade)
        self.assertEqual("SP", sigla)
        
    def test_alvorada(self):
        separador = SeparaNomeCidadeSiglaEstado("Alvorada do Norte (GO)")
        cidade, sigla = separador.separa()
        self.assertEqual("Alvorada do Norte", cidade)
        self.assertEqual("GO", sigla)
        
    def test_a_paraiba(self):
        separador = SeparaNomeCidadeSiglaEstado("Além Paraíba (MG)")
        cidade, sigla = separador.separa()
        self.assertEqual("Além Paraíba", cidade)
        self.assertEqual("MG", sigla)
        
    def test_exception1(self):
        with self.assertRaises(Exception):
            separador = SeparaNomeCidadeSiglaEstado("     ")
            cidade, sigla = separador.separa()

    def test_exception_mensagem(self):
        separador = SeparaNomeCidadeSiglaEstado("     ")
        with self.assertRaises(Exception) as context:
            separador = SeparaNomeCidadeSiglaEstado("     ")
            cidade, sigla = separador.separa()
        self.assertTrue('A string não está no formato correto: Nome da Cidade (AA)' in str(context.exception))
        
    def test_altonia(self):
        separador = SeparaNomeCidadeSiglaEstado("Altônia (PR")
        cidade, sigla = separador.separa()
        self.assertEqual("Altônia", cidade)
        self.assertEqual("PR", sigla)
