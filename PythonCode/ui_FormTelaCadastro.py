# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormTelaCadastrouxHKky.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_FormTelaCadastro(object):
    def setupUi(self, FormTelaCadastro):
        if not FormTelaCadastro.objectName():
            FormTelaCadastro.setObjectName(u"FormTelaCadastro")
        FormTelaCadastro.setEnabled(True)
        FormTelaCadastro.resize(800, 600)
        self.labelCadastro = QLabel(FormTelaCadastro)
        self.labelCadastro.setObjectName(u"labelCadastro")
        self.labelCadastro.setGeometry(QRect(320, 100, 191, 41))
        font = QFont()
        font.setPointSize(26)
        self.labelCadastro.setFont(font)
        self.frame = QFrame(FormTelaCadastro)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(160, 150, 461, 321))
        self.frame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame.setMouseTracking(False)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelNome = QLabel(self.frame_2)
        self.labelNome.setObjectName(u"labelNome")

        self.verticalLayout_3.addWidget(self.labelNome)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.lineEditNome = QLineEdit(self.frame_2)
        self.lineEditNome.setObjectName(u"lineEditNome")

        self.verticalLayout_3.addWidget(self.lineEditNome)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelSobrenome = QLabel(self.frame_4)
        self.labelSobrenome.setObjectName(u"labelSobrenome")

        self.verticalLayout_2.addWidget(self.labelSobrenome)

        self.lineEditSobrenome = QLineEdit(self.frame_4)
        self.lineEditSobrenome.setObjectName(u"lineEditSobrenome")

        self.verticalLayout_2.addWidget(self.lineEditSobrenome)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_5)

        self.labelEmail = QLabel(self.frame)
        self.labelEmail.setObjectName(u"labelEmail")

        self.verticalLayout.addWidget(self.labelEmail)

        self.lineEditEmail = QLineEdit(self.frame)
        self.lineEditEmail.setObjectName(u"lineEditEmail")

        self.verticalLayout.addWidget(self.lineEditEmail)

        self.labelSenha = QLabel(self.frame)
        self.labelSenha.setObjectName(u"labelSenha")

        self.verticalLayout.addWidget(self.labelSenha)

        self.lineEditSenha = QLineEdit(self.frame)
        self.lineEditSenha.setObjectName(u"lineEditSenha")
        self.lineEditSenha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lineEditSenha)

        self.labelConfirmarSenha = QLabel(self.frame)
        self.labelConfirmarSenha.setObjectName(u"labelConfirmarSenha")

        self.verticalLayout.addWidget(self.labelConfirmarSenha)

        self.lineEditConfirmarSenha = QLineEdit(self.frame)
        self.lineEditConfirmarSenha.setObjectName(u"lineEditConfirmarSenha")
        self.lineEditConfirmarSenha.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lineEditConfirmarSenha)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonSalvar = QPushButton(self.frame_6)
        self.pushButtonSalvar.setObjectName(u"pushButtonSalvar")

        self.horizontalLayout_2.addWidget(self.pushButtonSalvar)

        self.pushButtonCancelar = QPushButton(self.frame_6)
        self.pushButtonCancelar.setObjectName(u"pushButtonCancelar")

        self.horizontalLayout_2.addWidget(self.pushButtonCancelar)


        self.verticalLayout.addWidget(self.frame_6)

        self.pushButtonVoltarCadastro = QPushButton(FormTelaCadastro)
        self.pushButtonVoltarCadastro.setObjectName(u"pushButtonVoltarCadastro")
        self.pushButtonVoltarCadastro.setGeometry(QRect(170, 110, 75, 24))

        self.retranslateUi(FormTelaCadastro)

        QMetaObject.connectSlotsByName(FormTelaCadastro)
    # setupUi

    def retranslateUi(self, FormTelaCadastro):
        FormTelaCadastro.setWindowTitle(QCoreApplication.translate("FormTelaCadastro", u"Tela Cadastro", None))
        self.labelCadastro.setText(QCoreApplication.translate("FormTelaCadastro", u"Cadastro", None))
        self.labelNome.setText(QCoreApplication.translate("FormTelaCadastro", u"Nome", None))
        self.labelSobrenome.setText(QCoreApplication.translate("FormTelaCadastro", u"Sobrenome", None))
        self.labelEmail.setText(QCoreApplication.translate("FormTelaCadastro", u"Email", None))
        self.labelSenha.setText(QCoreApplication.translate("FormTelaCadastro", u"Senha", None))
        self.labelConfirmarSenha.setText(QCoreApplication.translate("FormTelaCadastro", u"Confirme a senha", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("FormTelaCadastro", u"Salvar", None))
        self.pushButtonCancelar.setText(QCoreApplication.translate("FormTelaCadastro", u"Cancelar", None))
        self.pushButtonVoltarCadastro.setText(QCoreApplication.translate("FormTelaCadastro", u"Voltar", None))
    # retranslateUi

