import sys
from PySide6 import QtWidgets
from ui_FormTelaAtendimento import  Ui_FormTelaAtendimento  # Importe a classe gerada

class TelaAtendimento(QtWidgets.QMainWindow, Ui_FormTelaAtendimento):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI
        self.pushButtonVoltarAtendimento.clicked.connect(self.voltar)
        
    def voltar(self):
        # Lógica para o botão "Voltar" para acessar a TelaFuncionarios.py"
        self.close()
        



# app = QtWidgets.QApplication(sys.argv)
# janela = TelaAtendimento()
# janela.show()
# sys.exit(app.exec_())