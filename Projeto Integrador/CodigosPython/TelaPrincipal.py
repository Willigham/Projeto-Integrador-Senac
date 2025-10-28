import sys
from PySide6 import QtWidgets
from ui_FormTelaPrincipal import  Ui_FormTelaPrincipal  # Importe a classe gerada
from Pessoa import Pessoa
from Item import Item

class TelaPrincipal(QtWidgets.QMainWindow, Ui_FormTelaPrincipal):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Método gerado para configurar a UI
        self.pushButtonInicio.clicked.connect(self.inicio)
        self.pushButtonEstoque.clicked.connect(self.estoque)
        self.pushButtonGerenciarUsuarios.clicked.connect(self.gerenciarUsuarios)
        self.pushButtonEditarPerfil.clicked.connect(self.editarPerfil)
        self.pushButtonSair.clicked.connect(self.sair)
        self.pushButtonAdicionarItem.clicked.connect(self.adicionarItem)
        self.pushButtonRemoverComida.clicked.connect(self.removerComida)
        self.pushButtonRemoverBebida.clicked.connect(self.removerBebida)
        self.pushButtonCancelarItem.clicked.connect(self.cancelarItem)
        self.Item = []  # Lista para armazenar todos os itens cadastrados

    # funcoes dos botoes da tela principal
    def inicio(self):
        paginaInicio = self.page_1Inicio
        self.stackedWidget.setCurrentWidget(paginaInicio)
    
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

    # funcoes dos botoes de adicionar e remover itens do tableWidgetComida e tableWidgetBebida
    def adicionarItem(self):
        nome = self.lineEditNomeItem.text()
        quantidade = self.lineEditQuantidadeItem.text()
        valor = self.lineEditValorItem.text()
        tipo = self.comboBoxItem.currentText()
        rowPositionComida = self.tableWidgetComida.rowCount()
        rowPositionBebida = self.tableWidgetBebida.rowCount()

        # validar campos vazios
        if not nome or not quantidade or not valor:
            QtWidgets.QMessageBox.warning(self, "Erro ao adicionar item", "Por favor, preencha todos os campos.")
            return
        
        # adicionar item na tabela correta com base no tipo selecionado
        if self.comboBoxItem.currentText() == "Tira Gosto":
            rowPositionComida = self.tableWidgetComida.rowCount()
            self.tableWidgetComida.insertRow(rowPositionComida)
            self.tableWidgetComida.setItem(rowPositionComida , 0, QtWidgets.QTableWidgetItem(nome))
            self.tableWidgetComida.setItem(rowPositionComida , 1, QtWidgets.QTableWidgetItem(valor))
            self.tableWidgetComida.setItem(rowPositionComida , 2, QtWidgets.QTableWidgetItem(quantidade))
        if self.comboBoxItem.currentText() == "Bebida":
            rowPositionBebida = self.tableWidgetBebida.rowCount()
            self.tableWidgetBebida.insertRow(rowPositionBebida)
            self.tableWidgetBebida.setItem(rowPositionBebida , 0, QtWidgets.QTableWidgetItem(nome))
            self.tableWidgetBebida.setItem(rowPositionBebida , 1, QtWidgets.QTableWidgetItem(valor))
            self.tableWidgetBebida.setItem(rowPositionBebida , 2, QtWidgets.QTableWidgetItem(quantidade))
        if self.comboBoxItem.currentText() == "Selecione...":
            QtWidgets.QMessageBox.warning(self, "Erro ao adicionar item", "Por favor, selecione um tipo de item válido.")
            return
            
        novo_item = Item(nome, quantidade, valor)
        novo_item.tipo = tipo
        self.Item.append(novo_item)
        self.lineEditNomeItem.clear()
        self.lineEditQuantidadeItem.clear()
        self.lineEditValorItem.clear()
        self.comboBoxItem.setCurrentIndex(0)

    # Função para remover Comida
    def removerComida(self):
        selectedRow = self.tableWidgetComida.currentRow()
        if selectedRow >= 0:
            reply = QtWidgets.QMessageBox.question(self, "Confirmação", "Tem certeza que deseja remover este item?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.tableWidgetComida.removeRow(selectedRow)
        else:
            QtWidgets.QMessageBox.warning(self, "Erro ao remover item", "Por favor, selecione um item para remover.")
            return
     # Função para remover Bebida
    def removerBebida(self):
        selectedRow = self.tableWidgetBebida.currentRow()
        if selectedRow >= 0:
            reply = QtWidgets.QMessageBox.question(self, "Confirmação", "Tem certeza que deseja remover este item?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.tableWidgetBebida.removeRow(selectedRow)
        else:
            QtWidgets.QMessageBox.warning(self, "Erro ao remover item", "Por favor, selecione um item para remover.")
            return
            
    def cancelarItem(self):
        self.lineEditNomeItem.clear()
        self.lineEditQuantidadeItem.clear()
        self.lineEditValorItem.clear()
    

        
            
    


# app = QtWidgets.QApplication(sys.argv)
# janela = TelaPrincipal()
# janela.show()
# sys.exit(app.exec_())