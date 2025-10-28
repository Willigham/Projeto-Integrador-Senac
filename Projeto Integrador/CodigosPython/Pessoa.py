class Pessoa:
    def __init__(self, nome, sobrenome, email, senha):
        self.id = ""
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.cargo = ""  # Pode ser "Administrador", "Gerente" ou "Funcionário"
    # Pessoas = []  # Lista para armazenar todas as pessoas cadastradas