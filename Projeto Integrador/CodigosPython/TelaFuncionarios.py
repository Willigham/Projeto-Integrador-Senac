import sys
from PySide6 import QtWidgets
from ui_FormTelaFuncionarios import  Ui_FormTelaFuncionarios  # Importe a classe gerada
from TelaAtendimento import TelaAtendimento

class TelaFuncionarios(QtWidgets.QMainWindow, Ui_FormTelaFuncionarios):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI
        self.pushButtonIniciarAtendimento.clicked.connect(self.atendimento)
        self.pushButtonSairGenreciadorNegocios.clicked.connect(self.sair)
    
        
    def atendimento(self):
        self.telaAtendimento = TelaAtendimento()
        self.telaAtendimento.show()

    def sair(self):
        self.close()
        
        

app = QtWidgets.QApplication(sys.argv)
janela = TelaFuncionarios()
janela.show()
sys.exit(app.exec_())