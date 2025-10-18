# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormTelaLoginegkToh.ui'
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

class Ui_FormTelaLogin(object):
    def setupUi(self, FormTelaLogin):
        if not FormTelaLogin.objectName():
            FormTelaLogin.setObjectName(u"FormTelaLogin")
        FormTelaLogin.resize(800, 600)
        self.frame = QFrame(FormTelaLogin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(180, 130, 401, 321))
        self.frame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame.setMouseTracking(False)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelLogin = QLabel(self.frame_7)
        self.labelLogin.setObjectName(u"labelLogin")
        font = QFont()
        font.setPointSize(26)
        self.labelLogin.setFont(font)
        self.labelLogin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelLogin)

        self.labelSubTexto = QLabel(self.frame_7)
        self.labelSubTexto.setObjectName(u"labelSubTexto")
        font1 = QFont()
        font1.setPointSize(10)
        self.labelSubTexto.setFont(font1)
        self.labelSubTexto.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_5.addWidget(self.labelSubTexto)

        self.labelEmail_2 = QLabel(self.frame_7)
        self.labelEmail_2.setObjectName(u"labelEmail_2")

        self.verticalLayout_5.addWidget(self.labelEmail_2)

        self.lineEditEmail_2 = QLineEdit(self.frame_7)
        self.lineEditEmail_2.setObjectName(u"lineEditEmail_2")

        self.verticalLayout_5.addWidget(self.lineEditEmail_2)

        self.labelSenha_2 = QLabel(self.frame_7)
        self.labelSenha_2.setObjectName(u"labelSenha_2")

        self.verticalLayout_5.addWidget(self.labelSenha_2)

        self.lineEditSenha_2 = QLineEdit(self.frame_7)
        self.lineEditSenha_2.setObjectName(u"lineEditSenha_2")
        self.lineEditSenha_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_5.addWidget(self.lineEditSenha_2)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)

        self.verticalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonEntrar = QPushButton(self.frame_11)
        self.pushButtonEntrar.setObjectName(u"pushButtonEntrar")

        self.horizontalLayout_4.addWidget(self.pushButtonEntrar)

        self.pushButtonCadastrarse = QPushButton(self.frame_11)
        self.pushButtonCadastrarse.setObjectName(u"pushButtonCadastrarse")

        self.horizontalLayout_4.addWidget(self.pushButtonCadastrarse)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.retranslateUi(FormTelaLogin)

        QMetaObject.connectSlotsByName(FormTelaLogin)
    # setupUi

    def retranslateUi(self, FormTelaLogin):
        FormTelaLogin.setWindowTitle(QCoreApplication.translate("FormTelaLogin", u"Tela Login", None))
        self.labelLogin.setText(QCoreApplication.translate("FormTelaLogin", u"Login", None))
        self.labelSubTexto.setText(QCoreApplication.translate("FormTelaLogin", u"Entre na sua conta", None))
        self.labelEmail_2.setText(QCoreApplication.translate("FormTelaLogin", u"Email", None))
        self.labelSenha_2.setText(QCoreApplication.translate("FormTelaLogin", u"Senha", None))
        self.pushButton.setText(QCoreApplication.translate("FormTelaLogin", u"Esqueci a senha", None))
        self.pushButtonEntrar.setText(QCoreApplication.translate("FormTelaLogin", u"Entrar", None))
        self.pushButtonCadastrarse.setText(QCoreApplication.translate("FormTelaLogin", u"Cadastrar-se", None))
    # retranslateUi

