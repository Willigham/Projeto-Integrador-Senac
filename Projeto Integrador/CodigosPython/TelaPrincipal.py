import sys
from PySide6 import QtWidgets
from ui_FormTelaPrincipal import  Ui_FormTelaPrincipal  # Importe a classe gerada

class TelaPrincipal(QtWidgets.QMainWindow, Ui_FormTelaPrincipal):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI
        self.pushButtonInicio.clicked.connect(self.inicio)
        self.pushButtonFinanceiro.clicked.connect(self.financeiro)
        self.pushButtonEstoque.clicked.connect(self.estoque)
        self.pushButtonGerenciarUsuarios.clicked.connect(self.gerenciarUsuarios)
        self.pushButtonEditarPerfil.clicked.connect(self.editarPerfil)
        self.pushButtonSair.clicked.connect(self.sair)

    def inicio(self):
        paginaInicio = self.page_1Inicio
        self.stackedWidget.setCurrentWidget(paginaInicio)
    
    def financeiro(self):
        paginaFinanceiro = self.page_2Financeiro    
        self.stackedWidget.setCurrentWidget(paginaFinanceiro)
    
    def estoque(self):
        paginaEstoque = self.page_3Estoque
        self.stackedWidget.setCurrentWidget(paginaEstoque)
    
    def gerenciarUsuarios(self):
        paginaGerenciarUsuarios = self.page_4GerenciarUsuarios
        self.stackedWidget.setCurrentWidget(paginaGerenciarUsuarios)

    def editarPerfil(self):
        paginaEditarPerfil = self.page_5EditarPerfil
        self.stackedWidget.setCurrentWidget(paginaEditarPerfil)
    
    def sair(self):
        self.close()


# app = QtWidgets.QApplication(sys.argv)
# janela = TelaPrincipal()
# janela.show()
# sys.exit(app.exec_())