def calcular_soma(num1, num2):
    return (num1 + num2)

def calcular_soma_negativo(num1, num2):
    return (num1 + num2)

def calcular_subtracao(num1, num2):
    return (num1 - num2)

def calcular_multiplicacao(num1, num2):
    return (num1 * num2)

def calcular_divisao(num1, num2):
    if num2 == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return (num1 / num2)