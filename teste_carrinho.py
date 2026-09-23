import unittest

from carrinho import Carrinho


class TestCarrinho(unittest.TestCase):

    def test_adicionar_item(self):
        resultado = Carrinho()
        resultado.adicionar_item("Arroz", 25)

        self.assertEqual(resultado.quantidade_itens(), 1)

    def test_remover_item(self):
        resultado = Carrinho()
        resultado.adicionar_item("Arroz", 25)
        resultado.remover_item("Arroz")

        self.assertEqual(resultado.quantidade_itens(), 0)

    def test_calcular_total(self):
        resultado = Carrinho()

        resultado.adicionar_item("Arroz", 25)
        resultado.adicionar_item("Feijão", 10)
        resultado.adicionar_item("Macarrão", 5)

        self.assertEqual(resultado.calcular_total(), 40)