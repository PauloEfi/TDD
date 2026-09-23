import unittest

from regras import calcular_desconto, calcular_desconto_vip, calcular_media, verificar_aprovacao

class TestRegrasNegocio(unittest.TestCase):

    def test_calcular_desconto(self):
        resultado = calcular_desconto(100)
        self.assertEqual(resultado, 90)

    def test_calcular_desconto_vip(self):
        resultado = calcular_desconto_vip(100)
        self.assertEqual(resultado, 80)

    def test_calcular_media(self):
        resultado = calcular_media(8, 7, 9)
        self.assertEqual(resultado, 8)

    def test_aluno_aprovado(self):
        resultado = verificar_aprovacao(7)
        self.assertTrue(resultado)

    def test_aluno_reprovado(self):
        resultado = verificar_aprovacao(6)
        self.assertFalse(resultado)