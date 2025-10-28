# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormTelaPrincipalppviuU.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_FormTelaPrincipal(object):
    def setupUi(self, FormTelaPrincipal):
        if not FormTelaPrincipal.objectName():
            FormTelaPrincipal.setObjectName(u"FormTelaPrincipal")
        FormTelaPrincipal.resize(800, 600)
        self.centralwidget = QWidget(FormTelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 20, 201, 361))
        self.frame.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelNomeUsuario = QLabel(self.frame)
        self.labelNomeUsuario.setObjectName(u"labelNomeUsuario")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelNomeUsuario.setFont(font)
        self.labelNomeUsuario.setFrameShape(QFrame.Shape.NoFrame)
        self.labelNomeUsuario.setFrameShadow(QFrame.Shadow.Plain)
        self.labelNomeUsuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelNomeUsuario)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButtonInicio = QPushButton(self.frame)
        self.pushButtonInicio.setObjectName(u"pushButtonInicio")

        self.verticalLayout.addWidget(self.pushButtonInicio)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButtonEstoque = QPushButton(self.frame)
        self.pushButtonEstoque.setObjectName(u"pushButtonEstoque")

        self.verticalLayout.addWidget(self.pushButtonEstoque)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.pushButtonGerenciarUsuarios = QPushButton(self.frame)
        self.pushButtonGerenciarUsuarios.setObjectName(u"pushButtonGerenciarUsuarios")

        self.verticalLayout.addWidget(self.pushButtonGerenciarUsuarios)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButtonEditarPerfil = QPushButton(self.frame)
        self.pushButtonEditarPerfil.setObjectName(u"pushButtonEditarPerfil")

        self.verticalLayout.addWidget(self.pushButtonEditarPerfil)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(200, 0, 591, 571))
        self.page_1Inicio = QWidget()
        self.page_1Inicio.setObjectName(u"page_1Inicio")
        self.labelBemVindo = QLabel(self.page_1Inicio)
        self.labelBemVindo.setObjectName(u"labelBemVindo")
        self.labelBemVindo.setGeometry(QRect(130, 130, 371, 161))
        font1 = QFont()
        font1.setPointSize(48)
        self.labelBemVindo.setFont(font1)
        self.labelNomeCargo_2 = QLabel(self.page_1Inicio)
        self.labelNomeCargo_2.setObjectName(u"labelNomeCargo_2")
        self.labelNomeCargo_2.setGeometry(QRect(190, 280, 201, 31))
        font2 = QFont()
        font2.setPointSize(20)
        self.labelNomeCargo_2.setFont(font2)
        self.labelNomeCargo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.page_1Inicio)
        self.page_2Financeiro = QWidget()
        self.page_2Financeiro.setObjectName(u"page_2Financeiro")
        self.stackedWidget.addWidget(self.page_2Financeiro)
        self.page_3Estoque = QWidget()
        self.page_3Estoque.setObjectName(u"page_3Estoque")
        self.tableWidgetComida = QTableWidget(self.page_3Estoque)
        if (self.tableWidgetComida.columnCount() < 3):
            self.tableWidgetComida.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetComida.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetComida.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetComida.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidgetComida.setObjectName(u"tableWidgetComida")
        self.tableWidgetComida.setGeometry(QRect(20, 50, 531, 171))
        self.labelEstoque = QLabel(self.page_3Estoque)
        self.labelEstoque.setObjectName(u"labelEstoque")
        self.labelEstoque.setGeometry(QRect(20, 10, 191, 41))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.labelEstoque.setFont(font3)
        self.tableWidgetBebida = QTableWidget(self.page_3Estoque)
        if (self.tableWidgetBebida.columnCount() < 3):
            self.tableWidgetBebida.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetBebida.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetBebida.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetBebida.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidgetBebida.setObjectName(u"tableWidgetBebida")
        self.tableWidgetBebida.setGeometry(QRect(20, 230, 531, 171))
        self.labelNomeItem = QLabel(self.page_3Estoque)
        self.labelNomeItem.setObjectName(u"labelNomeItem")
        self.labelNomeItem.setGeometry(QRect(20, 430, 81, 16))
        self.lineEditNomeItem = QLineEdit(self.page_3Estoque)
        self.lineEditNomeItem.setObjectName(u"lineEditNomeItem")
        self.lineEditNomeItem.setGeometry(QRect(20, 450, 571, 22))
        self.labelValorItem = QLabel(self.page_3Estoque)
        self.labelValorItem.setObjectName(u"labelValorItem")
        self.labelValorItem.setGeometry(QRect(20, 480, 81, 16))
        self.frame_9 = QFrame(self.page_3Estoque)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(400, 470, 191, 64))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelTipoItem = QLabel(self.frame_9)
        self.labelTipoItem.setObjectName(u"labelTipoItem")

        self.verticalLayout_6.addWidget(self.labelTipoItem)

        self.comboBoxItem = QComboBox(self.frame_9)
        self.comboBoxItem.addItem("")
        self.comboBoxItem.addItem("")
        self.comboBoxItem.addItem("")
        self.comboBoxItem.setObjectName(u"comboBoxItem")

        self.verticalLayout_6.addWidget(self.comboBoxItem)

        self.lineEditValorItem = QLineEdit(self.page_3Estoque)
        self.lineEditValorItem.setObjectName(u"lineEditValorItem")
        self.lineEditValorItem.setGeometry(QRect(20, 500, 151, 22))
        self.labelQuantidadeItem = QLabel(self.page_3Estoque)
        self.labelQuantidadeItem.setObjectName(u"labelQuantidadeItem")
        self.labelQuantidadeItem.setGeometry(QRect(220, 480, 71, 16))
        self.lineEditQuantidadeItem = QLineEdit(self.page_3Estoque)
        self.lineEditQuantidadeItem.setObjectName(u"lineEditQuantidadeItem")
        self.lineEditQuantidadeItem.setGeometry(QRect(220, 500, 151, 22))
        self.labelCadastrarItem = QLabel(self.page_3Estoque)
        self.labelCadastrarItem.setObjectName(u"labelCadastrarItem")
        self.labelCadastrarItem.setGeometry(QRect(220, 400, 141, 31))
        self.labelCadastrarItem.setFont(font3)
        self.pushButtonAdicionarItem = QPushButton(self.page_3Estoque)
        self.pushButtonAdicionarItem.setObjectName(u"pushButtonAdicionarItem")
        self.pushButtonAdicionarItem.setGeometry(QRect(20, 540, 281, 24))
        self.pushButtonCancelarItem = QPushButton(self.page_3Estoque)
        self.pushButtonCancelarItem.setObjectName(u"pushButtonCancelarItem")
        self.pushButtonCancelarItem.setGeometry(QRect(320, 540, 271, 24))
        self.pushButtonRemoverBebida = QPushButton(self.page_3Estoque)
        self.pushButtonRemoverBebida.setObjectName(u"pushButtonRemoverBebida")
        self.pushButtonRemoverBebida.setGeometry(QRect(550, 230, 31, 171))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.pushButtonRemoverBebida.setIcon(icon)
        self.pushButtonRemoverComida = QPushButton(self.page_3Estoque)
        self.pushButtonRemoverComida.setObjectName(u"pushButtonRemoverComida")
        self.pushButtonRemoverComida.setGeometry(QRect(550, 50, 31, 171))
        self.pushButtonRemoverComida.setIcon(icon)
        self.stackedWidget.addWidget(self.page_3Estoque)
        self.page_4GerenciarUsuarios = QWidget()
        self.page_4GerenciarUsuarios.setObjectName(u"page_4GerenciarUsuarios")
        self.tableWidgetUsuarios = QTableWidget(self.page_4GerenciarUsuarios)
        if (self.tableWidgetUsuarios.columnCount() < 3):
            self.tableWidgetUsuarios.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetUsuarios.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        font4 = QFont()
        font4.setPointSize(9)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.tableWidgetUsuarios.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidgetUsuarios.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.tableWidgetUsuarios.setObjectName(u"tableWidgetUsuarios")
        self.tableWidgetUsuarios.setGeometry(QRect(20, 130, 561, 381))
        self.labelGerenciarUsuarios = QLabel(self.page_4GerenciarUsuarios)
        self.labelGerenciarUsuarios.setObjectName(u"labelGerenciarUsuarios")
        self.labelGerenciarUsuarios.setGeometry(QRect(20, 70, 191, 41))
        self.labelGerenciarUsuarios.setFont(font3)
        self.frame_10 = QFrame(self.page_4GerenciarUsuarios)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(25, 520, 551, 44))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonAtualizar = QPushButton(self.frame_10)
        self.pushButtonAtualizar.setObjectName(u"pushButtonAtualizar")

        self.horizontalLayout_3.addWidget(self.pushButtonAtualizar)

        self.pushButtonEditar = QPushButton(self.frame_10)
        self.pushButtonEditar.setObjectName(u"pushButtonEditar")

        self.horizontalLayout_3.addWidget(self.pushButtonEditar)

        self.pushButtonExcluir = QPushButton(self.frame_10)
        self.pushButtonExcluir.setObjectName(u"pushButtonExcluir")

        self.horizontalLayout_3.addWidget(self.pushButtonExcluir)

        self.stackedWidget.addWidget(self.page_4GerenciarUsuarios)
        self.page_5EditarPerfil = QWidget()
        self.page_5EditarPerfil.setObjectName(u"page_5EditarPerfil")
        self.frame_2 = QFrame(self.page_5EditarPerfil)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 139, 521, 421))
        self.frame_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame_2.setMouseTracking(False)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelNome = QLabel(self.frame_3)
        self.labelNome.setObjectName(u"labelNome")

        self.verticalLayout_3.addWidget(self.labelNome)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frame_4)

        self.lineEditNome = QLineEdit(self.frame_3)
        self.lineEditNome.setObjectName(u"lineEditNome")

        self.verticalLayout_3.addWidget(self.lineEditNome)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelSobrenome = QLabel(self.frame_6)
        self.labelSobrenome.setObjectName(u"labelSobrenome")

        self.verticalLayout_4.addWidget(self.labelSobrenome)

        self.lineEditSobrenome = QLineEdit(self.frame_6)
        self.lineEditSobrenome.setObjectName(u"lineEditSobrenome")

        self.verticalLayout_4.addWidget(self.lineEditSobrenome)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelEmail = QLabel(self.frame_8)
        self.labelEmail.setObjectName(u"labelEmail")

        self.verticalLayout_5.addWidget(self.labelEmail)

        self.lineEditEmail = QLineEdit(self.frame_8)
        self.lineEditEmail.setObjectName(u"lineEditEmail")

        self.verticalLayout_5.addWidget(self.lineEditEmail)

        self.labelSenha = QLabel(self.frame_8)
        self.labelSenha.setObjectName(u"labelSenha")

        self.verticalLayout_5.addWidget(self.labelSenha)

        self.lineEditSenha = QLineEdit(self.frame_8)
        self.lineEditSenha.setObjectName(u"lineEditSenha")
        self.lineEditSenha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_5.addWidget(self.lineEditSenha)

        self.labelNovaSenha = QLabel(self.frame_8)
        self.labelNovaSenha.setObjectName(u"labelNovaSenha")

        self.verticalLayout_5.addWidget(self.labelNovaSenha)

        self.lineEditNovaSenha = QLineEdit(self.frame_8)
        self.lineEditNovaSenha.setObjectName(u"lineEditNovaSenha")
        self.lineEditNovaSenha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_5.addWidget(self.lineEditNovaSenha)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonSalvar = QPushButton(self.frame_7)
        self.pushButtonSalvar.setObjectName(u"pushButtonSalvar")

        self.horizontalLayout_2.addWidget(self.pushButtonSalvar)

        self.pushButtonCancelar = QPushButton(self.frame_7)
        self.pushButtonCancelar.setObjectName(u"pushButtonCancelar")

        self.horizontalLayout_2.addWidget(self.pushButtonCancelar)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.labelEditarPerfil = QLabel(self.page_5EditarPerfil)
        self.labelEditarPerfil.setObjectName(u"labelEditarPerfil")
        self.labelEditarPerfil.setGeometry(QRect(50, 70, 141, 41))
        self.labelEditarPerfil.setFont(font3)
        self.stackedWidget.addWidget(self.page_5EditarPerfil)
        self.pushButtonSair = QPushButton(self.centralwidget)
        self.pushButtonSair.setObjectName(u"pushButtonSair")
        self.pushButtonSair.setGeometry(QRect(10, 550, 183, 24))
        FormTelaPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FormTelaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        FormTelaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(FormTelaPrincipal)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormTelaPrincipal)
    # setupUi

    def retranslateUi(self, FormTelaPrincipal):
        FormTelaPrincipal.setWindowTitle(QCoreApplication.translate("FormTelaPrincipal", u"Tela Principal", None))
        self.labelNomeUsuario.setText(QCoreApplication.translate("FormTelaPrincipal", u"Adminstrador", None))
        self.pushButtonInicio.setText(QCoreApplication.translate("FormTelaPrincipal", u"Inicio", None))
        self.pushButtonEstoque.setText(QCoreApplication.translate("FormTelaPrincipal", u"Estoque", None))
        self.pushButtonGerenciarUsuarios.setText(QCoreApplication.translate("FormTelaPrincipal", u"Gerenciar Usu\u00e1rios", None))
        self.pushButtonEditarPerfil.setText(QCoreApplication.translate("FormTelaPrincipal", u"Editar Perfil", None))
        self.labelBemVindo.setText(QCoreApplication.translate("FormTelaPrincipal", u"Bem Vindo !", None))
        self.labelNomeCargo_2.setText(QCoreApplication.translate("FormTelaPrincipal", u"Administrador", None))
        ___qtablewidgetitem = self.tableWidgetComida.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormTelaPrincipal", u"TIRA GOSTO", None));
        ___qtablewidgetitem1 = self.tableWidgetComida.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormTelaPrincipal", u"VALOR", None));
        ___qtablewidgetitem2 = self.tableWidgetComida.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormTelaPrincipal", u"QUANTIDADE", None));
        self.labelEstoque.setText(QCoreApplication.translate("FormTelaPrincipal", u"Estoque", None))
        ___qtablewidgetitem3 = self.tableWidgetBebida.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormTelaPrincipal", u"BEBIDAS", None));
        ___qtablewidgetitem4 = self.tableWidgetBebida.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormTelaPrincipal", u"VALOR", None));
        ___qtablewidgetitem5 = self.tableWidgetBebida.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormTelaPrincipal", u"QUANTIDADE", None));
        self.labelNomeItem.setText(QCoreApplication.translate("FormTelaPrincipal", u"Nome do Item", None))
        self.labelValorItem.setText(QCoreApplication.translate("FormTelaPrincipal", u"Valor", None))
        self.labelTipoItem.setText(QCoreApplication.translate("FormTelaPrincipal", u"Tipo", None))
        self.comboBoxItem.setItemText(0, QCoreApplication.translate("FormTelaPrincipal", u"Selecione...", None))
        self.comboBoxItem.setItemText(1, QCoreApplication.translate("FormTelaPrincipal", u"Tira Gosto", None))
        self.comboBoxItem.setItemText(2, QCoreApplication.translate("FormTelaPrincipal", u"Bebida", None))

        self.labelQuantidadeItem.setText(QCoreApplication.translate("FormTelaPrincipal", u"Quantidade", None))
        self.labelCadastrarItem.setText(QCoreApplication.translate("FormTelaPrincipal", u"Cadastrar Item", None))
        self.pushButtonAdicionarItem.setText(QCoreApplication.translate("FormTelaPrincipal", u"ADICIONAR ITEM", None))
        self.pushButtonCancelarItem.setText(QCoreApplication.translate("FormTelaPrincipal", u"CANCELAR", None))
        self.pushButtonRemoverBebida.setText("")
        self.pushButtonRemoverComida.setText("")
        ___qtablewidgetitem6 = self.tableWidgetUsuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FormTelaPrincipal", u"NOME", None));
        ___qtablewidgetitem7 = self.tableWidgetUsuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("FormTelaPrincipal", u"EMAIL", None));
        ___qtablewidgetitem8 = self.tableWidgetUsuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("FormTelaPrincipal", u"CARGO", None));
        self.labelGerenciarUsuarios.setText(QCoreApplication.translate("FormTelaPrincipal", u"Gerenciar Usu\u00e1rios", None))
        self.pushButtonAtualizar.setText(QCoreApplication.translate("FormTelaPrincipal", u"Atualizar", None))
        self.pushButtonEditar.setText(QCoreApplication.translate("FormTelaPrincipal", u"Editar", None))
        self.pushButtonExcluir.setText(QCoreApplication.translate("FormTelaPrincipal", u"Excluir", None))
        self.labelNome.setText(QCoreApplication.translate("FormTelaPrincipal", u"Nome", None))
        self.labelSobrenome.setText(QCoreApplication.translate("FormTelaPrincipal", u"Sobrenome", None))
        self.labelEmail.setText(QCoreApplication.translate("FormTelaPrincipal", u"Email", None))
        self.labelSenha.setText(QCoreApplication.translate("FormTelaPrincipal", u"Senha", None))
        self.labelNovaSenha.setText(QCoreApplication.translate("FormTelaPrincipal", u"Nova senha", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("FormTelaPrincipal", u"Salvar", None))
        self.pushButtonCancelar.setText(QCoreApplication.translate("FormTelaPrincipal", u"Cancelar", None))
        self.labelEditarPerfil.setText(QCoreApplication.translate("FormTelaPrincipal", u"Editar Perfil", None))
        self.pushButtonSair.setText(QCoreApplication.translate("FormTelaPrincipal", u"SAIR", None))
    # retranslateUi

