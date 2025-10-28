import sys
from PySide6 import QtWidgets
from ui_FormTelaLogin import  Ui_FormTelaLogin  # Importe a classe gerada
from TelaPrincipal import TelaPrincipal
from TelaCadastro import TelaCadastro
from TelaFuncionarios import TelaFuncionarios


class TelaLogin(QtWidgets.QMainWindow, Ui_FormTelaLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI
        self.pushButtonEntrar.clicked.connect(self.entrar)
        self.pushButtonCadastrarSe.clicked.connect(self.cadastrarSe)

    # funcao para entrar na tela principal
    def entrar(self):

        # Obtendo os valores dos campos de email e senha
        email = self.lineEditEmail_2.text()
        senha = self.lineEditSenha_2.text()

        # Login válido
        if email == "admin" and senha == "admin":
            # Lógica para o botão "Entrar pra acessar a TelaPrincipal.py"
            self.tela_principal = TelaPrincipal()
            self.tela_principal.show()
            # limpar a caixa de textos
            

        elif email == "func" and senha == "func":
            # Lógica para o botão "Entrar pra acessar a TelaFuncionarios.py"
            from TelaFuncionarios import TelaFuncionarios
            self.tela_funcionarios = TelaFuncionarios()
            self.tela_funcionarios.show()
            
            
        
        # Login vazio
        elif email == "" or senha == "":
            QtWidgets.QMessageBox.warning(self, "Erro de Login", "Por favor, preencha todos os campos.")

        # Login inválido
        else:
            QtWidgets.QMessageBox.warning(self, "Erro de Login", "Email ou senha incorretos.")
            
        self.lineEditEmail_2.clear()
        self.lineEditSenha_2.clear()



    # funcao para abrir a tela de cadastro
    def cadastrarSe(self):
        # Lógica para o botão "Entrar pra acessar a Cadastro.py"
        self.tela_cadastro = TelaCadastro()
        self.tela_cadastro.show()
        


    

app = QtWidgets.QApplication(sys.argv)
janela = TelaLogin()
janela.show()
sys.exit(app.exec_())