import unittest

from login import login_valido, login_invalido, senha_vazia, cadastro_valido, cadastro_invalido, usuario_vazio

class TestLogin(unittest.TestCase):
    def test_login_valido(self):
        resultado = login_valido("usuario@gamil.com", "senha123")
        self.assertEqual(resultado, True)

def test_login_invalido(self):
        resultado = login_invalido("usuario@gamil.com", "123456")
        self.assertEqual(resultado, False)

def test_login_vazio(self):
        resultado = usuario_vazio("", "senha123")
        self.assertEqual(resultado, False)

def test_senha_vazia(self):
        resultado = senha_vazia("usuario@gamil.com", "")
        self.assertEqual(resultado, True)

def test_cadastro_valido(self):    
        resultado = cadastro_valido("novo_usuario@gamil.com", "nova_senha123")
        self.assertEqual(resultado, True)

def test_cadastro_invalido(self):    
            resultado = cadastro_invalido("falsousuario@gamil.com", "nova_senha123")
            self.assertEqual(resultado, False)


if __name__ =="__main__":
    unittest.main()