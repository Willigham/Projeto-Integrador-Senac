class Item:
    def __init__(self, nome, quantidade, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.tipo = []  # Pode ser "Tira-Gosto" ou "Bebida"
    # Itens = []  # Lista para armazenar todos os itens cadastrados