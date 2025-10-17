import sys
from PySide6 import QtWidgets
from ui_FormTelaCadastro import  Ui_FormTelaCadastro  # Importe a classe gerada

class TelaCadastro(QtWidgets.QMainWindow, Ui_FormTelaCadastro):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI

app = QtWidgets.QApplication(sys.argv)
janela = TelaCadastro()
janela.show()
sys.exit(app.exec_())