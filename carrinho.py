class Carrinho:

    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, preco):
        item = {
            "nome": nome,
            "preco": preco
        }

        self.itens.append(item)

    def remover_item(self, nome):
        self.itens = [
            item for item in self.itens
            if item["nome"] != nome
        ]

    def quantidade_itens(self):
        return len(self.itens)

    def calcular_total(self):
        total = 0

        for item in self.itens:
            total += item["preco"]

        return total