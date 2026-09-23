def login_valido(email, senha):
    return bool(email and senha and "@" in email and len(senha) >= 6)


def login_invalido(email, senha):
    return not login_valido(email, senha)


def usuario_vazio(email, senha):
    return not email and not senha


def senha_vazia(email, senha):
    return bool(email and not senha)


def cadastro_valido(email, senha):
    return bool(email and senha and "@" in email and len(senha) >= 6)


def cadastro_invalido(email, senha):
    return not cadastro_valido(email, senha)
