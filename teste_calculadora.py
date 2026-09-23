import unittest

from calculadora import calcular_soma, calcular_subtracao, calcular_multiplicacao, calcular_divisao

class TestCalculadora(unittest.TestCase):
    def test_calcular_soma(self):
        resultado = calcular_soma(2,3)
        self.assertEqual(resultado, 5)

    def test_calcular_soma_negativo(self):
        resultado = calcular_soma(5,-2)
        self.assertEqual(resultado, 3)

    def test_calcular_subtracao(self):
        resultado = calcular_subtracao(7,3)
        self.assertEqual(resultado, 4)

    def test_calcular_multiplicacao(self):
        resultado = calcular_multiplicacao(4,3)
        self.assertEqual(resultado, 12)

    def test_calcular_divisao(self):    
        resultado = calcular_divisao(10,2)
        self.assertEqual(resultado, 5)

    def test_calcular_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            calcular_divisao(10, 0)

if __name__ =="__main__":
    unittest.main()