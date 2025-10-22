import sys
from PySide6 import QtWidgets
from ui_FormTelaFuncionarios import  Ui_FormTelaFuncionarios  # Importe a classe gerada
from TelaAtendimento import TelaAtendimento
from TelaEstoque import TelaEstoque

class TelaFuncionarios(QtWidgets.QMainWindow, Ui_FormTelaFuncionarios):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI
        self.pushButtonIniciarAtendimento.clicked.connect(self.iniciarAtendimento)
        self.pushButtonSairGerenciadorNegocios.clicked.connect(self.sair)
        self.pushButtonConsultarEstoque.clicked.connect(self.consultarEstoque)


        
    def iniciarAtendimento(self):
        self.telaAtendimento = TelaAtendimento()
        self.telaAtendimento.show()

    def consultarEstoque(self):
        self.telaEstoque = TelaEstoque()
        self.telaEstoque.show()

    def sair(self):
        self.close()
        
        

# app = QtWidgets.QApplication(sys.argv)
# janela = TelaFuncionarios()
# janela.show()
# sys.exit(app.exec_())