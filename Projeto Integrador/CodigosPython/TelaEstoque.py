import sys
from PySide6 import QtWidgets
from ui_FormTelaEstoque import  Ui_FormTelaEstoque  # Importe a classe gerada

class TelaEstoque(QtWidgets.QMainWindow, Ui_FormTelaEstoque):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI
        



app = QtWidgets.QApplication(sys.argv)
janela = TelaEstoque()
janela.show()
sys.exit(app.exec_())