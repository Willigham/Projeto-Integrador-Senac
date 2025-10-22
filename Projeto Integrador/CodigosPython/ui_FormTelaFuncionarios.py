# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormTelaFuncionariosXzZakH.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_FormTelaFuncionarios(object):
    def setupUi(self, FormTelaFuncionarios):
        if not FormTelaFuncionarios.objectName():
            FormTelaFuncionarios.setObjectName(u"FormTelaFuncionarios")
        FormTelaFuncionarios.resize(800, 600)
        self.frame = QFrame(FormTelaFuncionarios)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(160, 230, 481, 191))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonIniciarAtendimento = QPushButton(self.frame)
        self.pushButtonIniciarAtendimento.setObjectName(u"pushButtonIniciarAtendimento")
        font = QFont()
        font.setPointSize(16)
        self.pushButtonIniciarAtendimento.setFont(font)

        self.verticalLayout.addWidget(self.pushButtonIniciarAtendimento)

        self.pushButtonConsultarEstoque = QPushButton(self.frame)
        self.pushButtonConsultarEstoque.setObjectName(u"pushButtonConsultarEstoque")
        self.pushButtonConsultarEstoque.setFont(font)

        self.verticalLayout.addWidget(self.pushButtonConsultarEstoque)

        self.pushButtonSairGenreciadorNegocios = QPushButton(FormTelaFuncionarios)
        self.pushButtonSairGenreciadorNegocios.setObjectName(u"pushButtonSairGenreciadorNegocios")
        self.pushButtonSairGenreciadorNegocios.setGeometry(QRect(160, 90, 75, 24))
        self.labelGerenciadorNegocios = QLabel(FormTelaFuncionarios)
        self.labelGerenciadorNegocios.setObjectName(u"labelGerenciadorNegocios")
        self.labelGerenciadorNegocios.setGeometry(QRect(160, 120, 481, 111))
        font1 = QFont()
        font1.setPointSize(26)
        self.labelGerenciadorNegocios.setFont(font1)
        self.labelGerenciadorNegocios.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelGerenciadorNegocios.raise_()
        self.frame.raise_()
        self.pushButtonSairGenreciadorNegocios.raise_()

        self.retranslateUi(FormTelaFuncionarios)

        QMetaObject.connectSlotsByName(FormTelaFuncionarios)
    # setupUi

    def retranslateUi(self, FormTelaFuncionarios):
        FormTelaFuncionarios.setWindowTitle(QCoreApplication.translate("FormTelaFuncionarios", u"Tela Funcionarios", None))
        self.pushButtonIniciarAtendimento.setText(QCoreApplication.translate("FormTelaFuncionarios", u"Iniciar Atendimento", None))
        self.pushButtonConsultarEstoque.setText(QCoreApplication.translate("FormTelaFuncionarios", u"Consultar Estoque", None))
        self.pushButtonSairGenreciadorNegocios.setText(QCoreApplication.translate("FormTelaFuncionarios", u"Sair", None))
        self.labelGerenciadorNegocios.setText(QCoreApplication.translate("FormTelaFuncionarios", u"Gerenciador de N\u00e9gocios", None))
    # retranslateUi

