import sys
from PySide6 import QtWidgets
from ui_FormTelaCadastro import  Ui_FormTelaCadastro  # Importe a classe gerada
from Pessoa import Pessoa

class TelaCadastro(QtWidgets.QMainWindow, Ui_FormTelaCadastro):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI
        self.pushButtonVoltarCadastro.clicked.connect(self.voltar)
        self.pushButtonSalvar.clicked.connect(self.SalvarCadastro)
        self.pushButtonCancelar.clicked.connect(self.cancelar)
        self.Pessoas = []  # Lista para armazenar todas as pessoas cadastradas

    def voltar(self):
        # Lógica para o botão "Voltar" para acessar a TelaLogin.py"
        self.close()
    
    def SalvarCadastro(self):
        # Obtendo os valores dos campos de cadastro
        nome = self.lineEditNome.text()
        sobrenome = self.lineEditSobrenome.text()
        email = self.lineEditEmail.text()
        senha = self.lineEditSenha.text()
        
        if senha != self.lineEditConfirmarSenha.text(): # Validação simples dos campos
            QtWidgets.QMessageBox.warning(self, "Erro de Cadastro", "As senhas não coincidem.")
            return
        elif not nome or not sobrenome or not email or not senha: # Verifica se algum campo está vazio
            QtWidgets.QMessageBox.warning(self, "Erro de Cadastro", "Por favor, preencha todos os campos.")
            return
        elif self.Pessoas:
            for pessoa in self.Pessoas: # Verifica se o email ou senha já estão cadastrados
                if pessoa.email == email or pessoa.senha == senha:
                    QtWidgets.QMessageBox.warning(self, "Erro de Cadastro", "Email ou senha já cadastrados.")
                    return
        
        # Criar uma nova instância de Pessoa e adicionar à lista
        nova_pessoa = Pessoa(nome, sobrenome, email, senha)
        self.Pessoas.append(nova_pessoa)
        QtWidgets.QMessageBox.information(self, "Cadastro Bem-Sucedido", "Usuário cadastrado com sucesso!")

        self.lineEditNome.clear()
        self.lineEditSobrenome.clear()
        self.lineEditEmail.clear()
        self.lineEditSenha.clear()
        self.lineEditConfirmarSenha.clear()


    def cancelar(self):
        self.lineEditNome.clear()
        self.lineEditSobrenome.clear()
        self.lineEditEmail.clear()
        self.lineEditSenha.clear()
        self.lineEditConfirmarSenha.clear()

    
    
        

# app = QtWidgets.QApplication(sys.argv)
# janela = TelaCadastro()
# janela.show()
# sys.exit(app.exec_())